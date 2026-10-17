⚠️ Don’t put every variable into a statistical regression model unless you know what you’re doing.

🔬 In my latest blog post, I use R simulations to show how adding highly correlated predictors can inflate the variance of coefficient estimates. The severity depends on the correlation level: stronger correlations make individual effects harder to estimate precisely.

📈 In one example, adding a highly correlated predictor increased an existing predictor’s standard error more than fivefold—even though R² barely changed.

💡 The takeaway: don’t add unnecessary variables. Have a sound reason to expect a variable to affect the response, or a clear reason to control for it when examining other predictors’ effects.

🎯 More variables don’t automatically make a model more informative.

👉 [Read the post, with R simulations and results](https://fortune9.netlify.app/2026/10/16/statistics-collinearity-in-regression/)

#Statistics #Regression #RStats #DataScience
