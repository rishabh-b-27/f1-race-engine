# F1 Race Engine - Project Journal

## Objective

Build a race prediction engine that combines historical F1 data,
driver ability, live car performance, weather, race state, tyres,
traffic, and other relevant factors to estimate race outcomes.

## Core Philosophy

The model should not attempt to perfectly reproduce the F1 teams'
private performance models.

Instead, the objective is to combine publicly available datasets
and statistical features into one coherent predictive system.

## Current Architecture

Raw Data
↓
Data Preparation
↓
Feature Engineering
↓
Prediction Model
↓
Race Simulation
↓
Prediction / Strategy Output

===================================================================

# Development Log

## 001 - Project Structure

### Files Created

- `src/data/`
- `src/features/`
- `src/models/`
- `src/simulation/`
- `src/strategy/`
- `tests/`

### Purpose

Created the basic architecture of the project.

The separation allows data loading, feature engineering,
modelling, simulation and strategy logic to remain independent.

### Key Learning

A project should be divided according to responsibilities
rather than putting everything into one large script.

===================================================================

## 002 - Race Data Loader

### File

`src/data/race_loader.py`

### Purpose

Loads a specific F1 race using FastF1.

Example:

`load_race(2025, "British Grand Prix")`

### Data Retrieved

- Lap data
- Weather data
- Race control messages
- Driver information
- Car data
- Position data

### Key Learning

FastF1 provides several different datasets belonging to the same
race session. These datasets have different timestamps and
different granularities.

### Validation

Tested using:

`tests/test_race_loader.py`

British Grand Prix loaded successfully with 20 drivers.

===================================================================

## 003 - Lap Data Preparation

### File

`src/data/prepare_laps.py`

### Purpose

Creates the main driver-lap dataset that will eventually become
the foundation for feature engineering.

### Important Columns

- Driver
- Team
- LapNumber
- LapTime
- Compound
- TyreLife
- Stint
- Time
- TrackStatus

### Key Learning

The raw FastF1 data is not immediately suitable for modelling.
It needs to be cleaned and structured first.

### Validation

Tested using:

`tests/test_race_loader.py`

===================================================================

## 004 - Dynamic Car Performance

### File

`src/features/car_performance.py`

### Purpose

Estimate relative constructor performance during the race.

The model does not assume that a constructor has a fixed performance
level throughout the race.

Instead, the race is divided into 10-lap windows.

For each window:

1. Calculate each team's mean lap time.
2. Identify the fastest team.
3. Calculate every team's relative pace delta.

Formula:

CarPerformanceDelta =
(TeamMeanLapTime - FastestTeamMeanLapTime)
/
FastestTeamMeanLapTime

### Example

If McLaren is fastest:

McLaren → 0.000
Red Bull → 0.0096
Ferrari → 0.0155

### Design Decision

Use 10-lap windows.

5 laps was considered too noisy.
15-20 laps was considered too coarse.

### Important Limitation

Raw lap times are affected by:

- Traffic
- Tyres
- Safety cars
- Weather
- Fuel
- Driver behaviour

Therefore this is an estimate of live relative car performance,
not a perfect measurement of underlying car pace.

### Validation

Tested using:

`tests/test_car_performance.py`

===================================================================

## 005 - Driver Rating

### File

`data/raw/driver_ratings.csv`

### Purpose

Provide a pre-existing quantitative estimate of driver ability.

The project uses driver ratings rather than attempting to construct
a driver ranking from scratch.

### Features

- OverallElo
- DryElo
- WetDelta

### Design Decision

Driver skill is treated as a major independent feature because
finishing position alone cannot separate driver performance from
constructor performance.

### Example

Max Verstappen:
OverallElo = 2040
DryElo = 2032
WetDelta = +18

### Important Assumption

The rating dataset is treated as an external estimate of driver
ability.

It is not claimed to be the objectively correct ranking of every
driver.

### Integration

`src/features/driver_features.py`

Driver ratings are attached to each driver's lap/race data.

===================================================================

## 006 - Weather Data

### File

`src/data/weather.py`

### Purpose

Extract weather observations from the FastF1 race session.

### Available Variables

- AirTemp
- TrackTemp
- Humidity
- Pressure
- Rainfall
- WindDirection
- WindSpeed

### Key Learning

Weather data is timestamp-based rather than directly indexed
by race lap.

Therefore weather observations must be aligned with lap timestamps
before being used as race features.

===================================================================

## 007 - Weather Alignment

### File

`src/features/weather_alignment.py`

### Purpose

Align timestamped weather observations with driver lap timestamps.

### Core Problem

Weather is observed approximately every minute, while laps occur
at different timestamps for different drivers.

Therefore a lap cannot simply be assigned the weather observation
with the same row number.

The correct approach is temporal alignment.

### Validation

Checked the first lap of each driver against the corresponding
weather observation.

===================================================================

## 008 - Race State Feature

### File
- `src/features/race_state.py`

### Purpose
Convert FastF1 TrackStatus values into a categorical race state.

### TrackStatus Interpretation

FastF1 can represent multiple chronological status changes
within one lap as a sequence.

Examples:

- `12` → GREEN → YELLOW
- `14` → GREEN → SC
- `41` → SC → GREEN
- `671` → VSC → VSC ending → GREEN
- `6712` → VSC → VSC ending → GREEN → YELLOW

The final status in the sequence is treated as the active
state for the lap.

### Mapping

- `1` → GREEN
- `2` → YELLOW
- `4` → SC
- `5` → RED
- `6` → VSC
- `7` → GREEN because VSC has ended

### Validation

Tested using the 2025 British Grand Prix.

Important transition cases:

- `6712` → YELLOW
- `671` → GREEN
- `67` → GREEN
- `41` → GREEN
- `124` → SC
- `126` → VSC

Feature successfully integrated into driver-lap data.

===================================================================

## 009 - Race Gaps

### File

`src/features/race_gaps.py`

### Purpose

Calculate the live race gaps between drivers based on their
position and cumulative race time.

### Features

- GapToLeader
- GapToAhead

### Definitions

**GapToLeader**

The difference between a driver's cumulative race time and the
leader's cumulative race time on the same lap.

**GapToAhead**

The difference between a driver's cumulative race time and the
cumulative race time of the car immediately ahead of them on the
same lap.

For the race leader:

- GapToLeader = 0
- GapToAhead = 0

### Calculation

For each lap:

1. Select drivers with valid Position and Time values.
2. Sort drivers by race position.
3. Identify the leader.
4. Calculate each driver's time difference from the leader.
5. Identify the driver one position ahead.
6. Calculate the time difference to that driver.

### Design Decision

Only two gap features are retained:

- GapToLeader
- GapToAhead

A separate gap-to-previous-car feature is unnecessary because
GapToAhead already represents the gap to the car immediately
ahead.

### Important Limitation

These gaps are derived from cumulative lap timestamps rather than
official F1 timing gaps.

Therefore they may differ from official timing data during:

- Safety Car periods
- Virtual Safety Car periods
- Pit stops
- Lapped traffic
- Other timing irregularities

### Validation

Tested using the 2025 British Grand Prix.

Validation included:

- Full race gap output
- Lap 1 sorted by position
- Lap 20 sorted by position
- Driver-specific gap progression

The resulting values behaved as expected, with the leader having
zero gap and each following driver's GapToAhead representing the
time difference to the car immediately ahead.

===================================================================

## 010 - Ten-Lap Position Prediction Target

### File

`src/features/target.py`

### Purpose

Define the machine-learning target as the driver's race position
10 laps after the current lap.

For a driver at lap `t`:

`Target = position at lap t+10`

This turns the problem into a rolling short-horizon prediction task
rather than directly predicting the final race result.

### Target Classes

- `1` → P1 after 10 laps
- `2` → P2 after 10 laps
- `3` → P3 after 10 laps
- `4` → P4 after 10 laps
- `5` → P5 after 10 laps
- `6` → P6 after 10 laps
- `7` → P7 after 10 laps
- `8` → P8 after 10 laps
- `9` → P9 or worse after 10 laps
- `10` → DNF before the target horizon

DNS rows are excluded from training.

Rows without a valid future target are excluded.

### Design Decision

The model predicts one mutually exclusive probability distribution.

Therefore:

`P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9+ + P(DNF) = 1`

This gives the model a probability distribution over the driver's
possible outcome after the next 10 laps.

### Validation

Tested using the 2025 British Grand Prix.

Special cases checked:

- Normal finishing positions
- P9+ grouping
- Retired drivers
- Drivers who did not start
- Drivers still classified as racing/lapped

===================================================================

## 011 - Multi-Race Training Dataset

### Files

- `src/data/build_training_data.py`
- `src/data/model_dataset.py`
- `src/data/multi_race_dataset.py`

### Purpose

Create a reusable pipeline for converting individual race sessions
into machine-learning datasets and combining multiple races for
training.

### Pipeline

`Race Session`
↓
`build_training_data()`
↓
`build_model_dataset()`
↓
`X, y`
↓
`multi_race_dataset`
↓
`Model Training`

### Important Design Decisions

Future target columns are excluded from the feature matrix.

Categorical variables are converted into numerical representations.

Timedeltas such as lap and sector times are converted into numerical
seconds before model training.

Only rows with valid training targets are included.

### Validation

The British Grand Prix produced:

- 825 total driver-lap rows
- 675 usable training rows

The resulting dataset contained the ten target classes.

===================================================================

## 012 - V1 Baseline Model

### Files

- `src/models/baseline.py`
- `src/models/calibrated.py`
- `src/models/validation.py`

### Model

Random Forest multiclass classifier.

Configuration:

- 300 trees
- `min_samples_leaf = 2`
- `random_state = 42`
- `n_jobs = -1`

### Probability Output

The model uses `predict_proba()` to produce a complete probability
distribution over the ten possible target classes.

Example:

`P(P1), P(P2), ..., P(P8), P(P9+), P(DNF)`

The probabilities sum to 1.

### Calibration

A calibrated Random Forest was tested because probability quality is
more important than raw classification accuracy for the intended
prediction engine.

Initial British Grand Prix comparison:

| Model | Accuracy | Log Loss |
|---|---:|---:|
| Random Forest | 49.19% | 2.012 |
| Calibrated Random Forest | 50.22% | 1.788 |

Calibration therefore improved both accuracy and log loss in this
experiment.

### Baselines

Current-position baseline:

- Accuracy = 51.41%
- Log Loss = 17.515

Class-frequency baseline:

- Accuracy = 46.37%
- Log Loss = 1.915

The calibrated Random Forest produced substantially better log loss
than the current-position baseline and improved on the class-frequency
baseline in the initial experiment.

===================================================================

## 013 - Rolling Race Validation

### Purpose

Evaluate the model on races that were not used for training.

The validation strategy is chronological rather than random.

Earlier races are used for training and a later race is held out for
testing.

This reduces leakage caused by mixing laps from the same race between
training and testing.

### Validation

The model was evaluated across multiple 2025 races, including:

- Bahrain Grand Prix
- Saudi Arabian Grand Prix
- British Grand Prix

The final rolling validation benchmark was:

**Average Accuracy: 59.80%**

**Average Log Loss: 1.364**

### Interpretation

The model demonstrates meaningful predictive signal on unseen races.

However, the benchmark is treated as a V1 baseline rather than a
finished model.

The goal of future development is to improve the model's understanding
of race dynamics while preserving the same validation protocol.

### V1 Checkpoint

**59.80% Average Accuracy**

**1.364 Average Log Loss**

This checkpoint should remain unchanged and be used as the benchmark
for all future feature and model experiments.

===================================================================

## 014 - Next Development Phase: Temporal Features

### Objective

The next phase is to add information about how a driver's race
position has been changing over time.

### First Feature Group

Planned features:

- `PositionChange3`
- `PositionChange5`
- `AveragePosition3`
- `AveragePosition5`
- `AveragePosition10`

These features should capture short-term position momentum and recent
race trajectory.

### Development Rule

Features will be introduced in small groups.

Each experiment will use the same rolling race validation procedure.

A feature group should only be retained if it provides measurable
improvement over the V1 benchmark.

### Current Benchmark

Accuracy: **59.80%**

Log Loss: **1.364**

===================================================================



===================================================================


# Open Questions

- How should traffic affect lap time?
- How should pit laps be identified?
- How should fuel load be approximated?
- How should tyre degradation interact with car performance?
- Should driver rating be static or updated over time?
- How should DNFs be represented?
- How should weather transitions affect driver performance?
- How should Safety Car laps affect car-performance estimation?
- How should qualifying position influence race prediction?

===================================================================


