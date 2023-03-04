# Cyberbullying Tweet Prediction

This project aims to built, test and select a Natural Language Processing model that has optimal performance to predict cyberbullying type of tweets from an account

# File Explanation on Github

This repository consists of several files, namely :

- Folder `deployment` = Contains files used for *deployment* to `HuggingFace` (contains models, python applications etc.)
- `notebook_Cyberbullying-Tweet-Prediction.ipynb` = This file is the main *notebook* used to explore dataset and built model
- `inferencing_Cyberbullying-Tweet-Prediction.ipynb`= *Notebook* used for *testing inference*. Inferencing is done on a separate *notebook* to prove that the model can run on a *notebook* that is *clean* of variables
- `url.txt` = Deployment URL to HuggingFace

# Brief Summary of Project

The flow of this *project*, first EDA (*Exploratory Data Analysis*) to find out the basic picture of the *dataset*. Second, *cleaning* and *preprocessing* of the *dataset*. Third, Built 4 Model (LSTM, LSTM Improvement, GRU, GRU Transfer Learning) and choose LSTM Improvement as Best Model. Result of the model using Deep Learning with own architecture shows 77% Accuracy on test-set


# Project Conclusion

Strength

1. Has an accuracy of 77% (above 70%) which means that this model can classify *tweets* well.
2. This model is not affected by *treshold*
3. Other than `not_cyberbullying` class and `cyberbullying` class, the prediction error is quite low (in the range of 100 tweets down. Notes: the total dataset is 44.000 tweets)

Weaknesses

1. The model is less accurate in predicting the `not_cyberbullying` class and `cyberbullying` class.
2. Has a long *training* time if you want to update the data 

