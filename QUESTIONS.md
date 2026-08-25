
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

## Advanced ML / Statistical Defense

219. What is the difference between aleatoric and epistemic uncertainty?

220. Which type of uncertainty is more relevant to this prediction problem?

221. How would you estimate uncertainty in a Random Forest?

222. Why is a Random Forest's class probability not automatically a statistically valid probability?

223. What is a proper scoring rule?

224. Why is log loss a proper scoring rule?

225. What is the Brier score?

226. How would Brier score complement log loss?

227. What is calibration error?

228. What is a reliability diagram?

229. How would you determine whether the calibrated model is actually better calibrated?

230. What is cross-validation?

231. Why can ordinary k-fold cross-validation be inappropriate for race data?

232. What is nested cross-validation?

233. When would nested cross-validation be useful here?

234. What is hyperparameter overfitting?

235. Can you overfit your validation set without overfitting your training data?

236. How would you tune hyperparameters without contaminating the test race?

237. Why should the final test race be touched only once?

238. What is a confidence interval?

239. How would you calculate a confidence interval for race-level accuracy?

240. Why are individual driver-lap samples not necessarily independent?

241. Why does temporal and driver-level correlation matter statistically?

242. What is bootstrap resampling?

243. How could bootstrap be used to estimate uncertainty in model performance?

244. Why might ordinary bootstrap still be problematic for time-series data?

245. What is block bootstrap?

246. How could you compare two models statistically across multiple races?

247. What is a paired comparison?

248. Why is comparing models on exactly the same samples important?

249. What is statistical significance?

250. Why is statistical significance not the same as practical significance?


## Advanced Target / Probability Design

251. Why is P9+ an information-loss tradeoff?

252. What alternative target representations could preserve more information?

253. What would happen if you created 20 classes instead of 10?

254. What would happen to class imbalance with 20 classes?

255. Why might ordinal classification be better than ordinary multiclass classification?

256. What makes finishing position an ordinal variable?

257. Why does predicting P3 versus P4 have a different relationship than predicting P3 versus P20?

258. How could you exploit the ordinal structure mathematically?

259. What is a cumulative-link model?

260. Could you model P(position <= k) instead of exact position?

261. How would you recover exact-position probabilities from cumulative probabilities?

262. How would you represent DNF without destroying the ordinal structure?

263. Should DNF be modeled jointly with finishing position or separately?

264. What are the advantages of a two-stage model: DNF first, finishing position second?

265. What are the disadvantages of a two-stage model?

266. How would you combine DNF probability with conditional finishing-position probabilities?

267. What does a complete probability distribution over finishing positions actually represent?

268. Why is predicting the most likely position not enough?

269. Why can expected finishing position be misleading?

270. How would you calculate expected finishing position from the probability distribution?


## Race-Level Modeling

271. Why are driver outcomes not independent?

272. If one driver gains a position, what must happen to another driver?

273. Why does an independent driver model violate race mechanics?

274. How could you enforce the one-driver-per-position constraint?

275. What is a permutation distribution?

276. How could you model the final race order as a probability distribution over permutations?

277. Why is the space of possible race orders enormous?

278. How could Monte Carlo simulation approximate the race-order distribution?

279. What would one Monte Carlo race simulation contain?

280. How would you model lap-by-lap transitions in a simulation?

281. What is a state-transition model?

282. Could the race be represented as a Markov process?

283. What assumptions would a Markov model make?

284. Why might the Markov assumption be unrealistic for F1?

285. What information would need to be included in the state?

286. How would you model an overtake as a probabilistic event?

287. What factors influence overtaking probability?

288. How would DRS affect an overtaking model?

289. How would track characteristics affect overtaking probability?

290. How would you distinguish a genuine overtake from a position change caused by a pit stop?


## Advanced F1 Modeling

291. How would you estimate fuel load from observed lap times?

292. How would fuel burn affect lap-time trends?

293. Why can using raw lap times confuse fuel effects with car performance?

294. How would you separate tyre degradation from fuel burn?

295. How would you identify pit-stop strategy from lap data?

296. How could pit strategy be incorporated into future-position prediction?

297. How would you model Safety Car probability?

298. How would you incorporate an uncertain future Safety Car into predictions?

299. How would you incorporate weather forecasts while avoiding future leakage?

300. If you rebuilt V1 from scratch, what would you change first and why?


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

