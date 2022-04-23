## About

SC1015 Mini-Project focusing on Steam games, with data retrieved from SteamSpy or Steam's API.

- Main dataset gathered May 2019 from: https://www.kaggle.com/datasets/nikdavis/steam-store-raw
- Secondary dataset: https://steam.internet.byu.edu/ (SQL file)

## Files
SC1015 Mini-Project
- steamdata_clean.csv -> Cleaned Dataset from main dataset
- playergames.csv -> Cleaned dataset retireved from secondary dataset
- Steam - Data Cleaning.ipynb -> Contains Data cleaning to clean the dataset
- Steam - EDA + Modelling.ipynb -> Contains EDA and Modelling to answer - "How can we tell whether a game is good?"
- Steam - Game Recommendation System.ipynb -> Contains model and recommendation system to answer - "How do we find games that are good for us?"

## Contributors
SC2 Team 7
- @bryan9898 Bryan - Extracting Data, EDA, Classification, Recommender
- @kakapoot Yu Juan - Data Cleaning, EDA, Regression, Classification
- @chowweijie Wei Jie - EDA, Modelling, Presentation

## Problem Definition
- How can we tell whether a game is good? 
- How do we find games that are good for us?

## Models Used
- Linear Regression, KNN Regression, Random Forest Regression
- Gradient Boosting with Hyperparameter Optimisation
- Logistic Regression, Random Forest Classification
- TF-IDF (Term Frequency-Inverse Document Frequency) / CountVectorizer with Cosine Similarity
- Truncated SVD (Singular Value Decomposition) with t-SNE (t-Distributed Stochastic Neighbor Embedding)

## Conclusion
How can we tell whether a game is good? 
- In predicting the goodness of a game, our classification models have much higher accuracies than our regression models. This is possibly because it is easier to make accurate predictions for discrete values (game is good or not) rather than continuous values (rating).
- For regression, the best model for our dataset in predicting the rating of a game is a Gradient Boosted Regressor. For classification, the Random Forest Classifier performs better in predicting whether a game is good or not.
- Using regression, we are unable to accurately predict the rating of a game (~30% accuracy) using our current dataset. The current features that we have investigated (eg. genres, descriptions) do not have much influence on the rating of a game. Currently, some of the most important features of a good game are price, controller support, high platform and language support. We may need other factors (that the data might not be as easily accessible) to make better predictions, such as budget of the game.
- In the game industry, the number of games and the number of good games have both been increasing exponentially over the years. But, there is an increasingly huge proportion of smaller games made by indie devs that are of lower quality. This may also be skewing our data.

How do we find games that are good for us?
- We were able to create game recommendation systems, using Content-Based Recommendation and Collaborative Filtering.

## What did we learn from this project?
- Statistical methods eg. Wilson Confidence Interval, Bayesian Averaging
- Methods to handle data by normalizing/scaling/resampling/feature selection/etc. eg. StandardScaler, SMOTE, SelectKBest
- New models eg. KNN, SVD
- Gradient Boosting
- Cross Validation using GridSearchCV and KFold 
- Other packages eg. ast, requests, json, nltk
- Setting up of SQL server and database query
- API Usage (https://steamcommunity.com/dev)

## References

- <https://medium.com/hacking-and-gonzo/how-reddit-ranking-algorithms-work-ef111e33d0d9>
- <https://stackoverflow.com/questions/54357300/bayesian-averaging-in-a-dataframe>
- <https://machinelearningmastery.com/k-fold-cross-validation/>
- <https://www.datatechnotes.com/2021/02/seleckbest-feature-selection-example-in-python.html>
- <https://jazpeng.github.io/predict_movie_ratings/>
- <https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/>
- <https://medium.com/web-mining-is688-spring-2021/predicting-imdb-ratings-of-new-movies-2b39459fee9a>
- <https://towardsdatascience.com/time-series-forecasting-using-auto-arima-in-python-bb83e49210cd>
- <https://www.analyticsvidhya.com/blog/2020/10/overcoming-class-imbalance-using-smote-techniques/>
- <https://www.scikit-yb.org/en/latest/api/classifier/classification_report.html>
- <https://arxiv.org/pdf/1805.11372.pdf>
- <https://www.datacamp.com/community/tutorials/recommender-systems-python>
