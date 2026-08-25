
# F1 Race Engine - Technical Defense Questions



## Project Fundamentals



1. What exactly is the F1 Race Engine trying to predict?

2. Why predict the driver's position 10 laps into the future?

3. Why choose a 10-lap prediction horizon?

4. What does one training sample represent?

5. What information is available at prediction time?

6. What information must never be available to the model?

7. Why is this a classification problem?

8. Could this instead be regression?

9. Could this instead be ranking?



## Target Design



10. How is PositionTarget10 calculated?

11. Why are P1-P8 represented individually?

12. Why is P9+ grouped?

13. Why is DNF represented separately?

14. Why must the probabilities sum to 1?

15. Why use one multiclass model instead of eight binary models?

16. How are retired drivers handled?

17. How are DNS drivers handled?

18. What happens when t+10 does not exist?

19. What information is lost by grouping P9-P20?



## Data Leakage



20. What is data leakage?

21. Give an example of leakage in this project.

22. Why would final race position be leakage?

23. Why would future lap time be leakage?

24. Why must features at lap t only contain information available at lap t?

25. Why is random train/test splitting dangerous?

26. What is temporal leakage?

27. Why is chronological validation necessary?



## FastF1 / Data Pipeline



28. What does FastF1 provide?

29. Why use a preparation layer?

30. Why use DataFrame.copy()?

31. What is merge_asof()?

32. Why use backward alignment for weather?

33. What happens when weather data is sparse?

34. Why are some values represented as timedeltas?

35. Why must timedeltas be converted before scikit-learn training?



## Race State



36. What is TrackStatus?

37. Why is race state useful?

38. How does Safety Car affect lap times?

39. How does VSC affect lap times?

40. How can race state create misleading features?



## Race Gaps



41. How is GapToLeader calculated?

42. How is GapToAhead calculated?

43. Why are gaps useful?

44. Why might gap trend be more informative than absolute gap?

45. What happens to gaps during pit stops?



## Car Performance



46. What does CarPerformanceDelta represent?

47. Why calculate relative team performance?

48. Why use 10-lap windows?

49. What happens with a 1-lap window?

50. What happens with a 20-lap window?

51. What is the bias-variance tradeoff here?

52. Why can raw lap time be misleading?

53. How do tyres, fuel, traffic, weather, and Safety Car affect lap time?

54. Why isn't CarPerformanceDelta a pure measure of car performance?



## Driver Ratings



55. What is Elo?

56. Why use an Elo-style rating?

57. What does OverallElo represent?

58. What does DryElo represent?

59. What does WetDelta represent?

60. Could driver ratings introduce leakage?

61. How would you build your own driver rating?



## Tyres



62. What is TyreLife?

63. What is Stint?

64. What is Compound?

65. Why does tyre age matter?

66. What is tyre degradation?

67. How did you estimate degradation?

68. What confounding variables affect degradation?

69. How would you build a better degradation model?



## Feature Engineering



70. Why is feature engineering important?

71. Why use position momentum?

72. What does PositionChange3 mean?

73. What does PositionChange5 mean?

74. What does AveragePosition3 mean?

75. What does AveragePosition5 mean?

76. What does AveragePosition10 mean?

77. How do you prevent rolling features from looking into the future?

78. Why might pace trend be more useful than absolute pace?

79. What interaction effects might matter?



## Machine Learning



80. What is supervised learning?

81. What is multiclass classification?

82. What is a decision tree?

83. What is Random Forest?

84. What is bagging?

85. Why does Random Forest use many trees?

86. Why does averaging trees reduce variance?

87. What is overfitting?

88. What is underfitting?

89. What does min_samples_leaf do?

90. What does max_depth do?

91. What does n_estimators do?

92. What does random_state do?

93. What does n_jobs=-1 do?

94. What is the bias-variance tradeoff?

95. What are Random Forest's weaknesses?

96. Why not immediately use XGBoost or LightGBM?

97. Why not immediately use a neural network?



## Probabilities and Calibration



98. What does predict_proba() return?

99. Why do probabilities sum to 1?

100. What is probability calibration?

101. Why can Random Forest probabilities be poorly calibrated?

102. What is CalibratedClassifierCV?

103. What is sigmoid calibration?

104. What is isotonic calibration?

105. Why is calibration important for this project?

106. What is the difference between accuracy and probability quality?



## Evaluation



107. What is accuracy?

108. What is log loss?

109. Why is lower log loss better?

110. Why is log loss important for this project?

111. What happens to log loss when the model confidently predicts the wrong class?

112. Why did the current-position baseline have terrible log loss?

113. Why did the class-frequency baseline perform well?

114. What is class imbalance?

115. What is a naive baseline?

116. Why must every model beat a baseline?

117. What is chronological validation?

118. What is rolling validation?

119. Why is one held-out race insufficient?

120. What does the 59.80% / 1.364 benchmark actually mean?

121. Can you claim future races will achieve 59.8% accuracy?

122. What is distribution shift?



## Statistics



123. What is correlation?

124. Why does correlation not imply causation?

125. What are confounding variables?

126. Give an example of confounding in F1 lap time.

127. What is sampling bias?

128. What is variance?

129. What is uncertainty?

130. Why are model probabilities not guarantees?

131. How would you determine whether a feature improvement is statistically meaningful?



## Software Engineering



132. Why separate data, features, models, and tests?

133. What is separation of concerns?

134. What is modularity?

135. Why are tests important?

136. What should a unit test verify?

137. What should an integration test verify?

138. Why use Git?

139. Why preserve the V1 benchmark?

140. Why should experiments be reproducible?

141. Why use random_state=42?

142. Why should .venv not be committed?



## Python / Pandas



143. What is a DataFrame?

144. What is a Series?

145. Why use copy()?

146. What does groupby() do?

147. What does merge() do?

148. What is a left join?

149. What does merge_asof() do?

150. What is the difference between loc and iloc?

151. What does dropna() do?

152. What does notna() do?

153. What does get_dummies() do?

154. Why encode categorical variables?

155. Why can duplicate DataFrame columns cause problems?

156. Why did pandas throw the duplicate-label reindexing error?

157. Why did scikit-learn reject timedelta columns?



## Hard Design Questions



158. Why predict position instead of race time?

159. Why not predict final position directly?

160. Why not model every pair of drivers?

161. Why not use an LSTM?

162. Why not use a Transformer?

163. Why not use reinforcement learning?

164. Why not simulate the entire race?

165. Why not randomly split driver-laps?

166. Why not use qualifying position?

167. Why not use championship standings?

168. How would you handle regulation changes?

169. How would you handle a new driver?

170. How would you handle a new team?

171. How would you handle a new circuit?

172. How would you handle rain during the prediction horizon?

173. How would you handle a Safety Car appearing immediately after prediction?



## Very Hard Questions



174. What is the strongest criticism of your current model?

175. What assumption is most likely to be wrong?

176. What is the biggest leakage risk?

177. Which feature provides the most predictive signal?

178. How do you know that feature provides real signal?

179. What experiment would prove a feature useless?

180. What would make you reject Random Forest?

181. What would make you reject the 10-lap horizon?

182. What would make you change the target formulation?

183. If accuracy improves but log loss worsens, what does that mean?

184. If log loss improves but accuracy decreases, is that good?

185. If the model predicts P1 with 90% probability and loses, was it necessarily bad?

186. How do you know the model is learning race dynamics rather than dataset artifacts?

187. What would convince you the model generalizes?

188. What would you do if 2025 performs well but 2026 performs poorly?

189. How would you detect concept drift?

190. How would you retrain during a season?



## Future Modeling



191. How would you model all 20 finishing positions?

192. How would you model DNF probability independently?

193. How could you produce a complete race-order distribution?

194. How could you ensure predicted driver positions are physically consistent?

195. How would you prevent two drivers from both having 90% probability of P1?

196. How would you model correlations between drivers?

197. How would you model overtakes?

198. How would you incorporate pit-stop strategy?

199. How would you incorporate fuel load?

200. How would you incorporate weather forecasts?

201. How would you build a live prediction system that updates every lap?

202. How would you evaluate predictions continuously during a race?

203. What would a production architecture look like?



## Must Answer Without Looking at Code



204. What is the prediction target?

205. Why is it a 10-class classification problem?

206. Why is P9+ grouped?

207. How is DNF handled?

208. What prevents future information from entering features?

209. Why is chronological validation necessary?

210. Why is log loss important?

211. Why was Random Forest chosen?

212. Why is calibration necessary?

213. What does the 59.80% / 1.364 benchmark mean?

214. What are the biggest weaknesses of V1?

215. What feature would you build next?

216. How would you improve the model?

217. How would you prove an improvement is real?

218. How would you extend the model to all 20 positions?



## Defense Rule



Never answer:



"I don't know, the model just does that."



Instead explain:



- the underlying concept

- the implementation

- the reason for the design choice

- the assumption

- the limitation

- how it could be tested or improved



If I cannot explain a major part of this project from first principles,

I do not fully understand the project yet.

