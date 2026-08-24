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


