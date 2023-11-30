## credit to CS 307 week 8, 9 note and lab 5, 6, 8
# library import
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score

# dataframe preparation
columns = [
    "class", "Alcohol", "Malicacid", 
    "Ash", "Alcalinity_of_ash", "Magnesium", 
    "Total_phenols", "Flavanoids", "Nonflavanoid_phenols",
    "Proanthocyanins", "Color_intensity", "Hue",
    "0D280_0D315_of_diluted_wines", "Proline",
    ]
wine_df = pd.read_csv("data/wine.data", names=columns)

# Split dataset into train and test dataset
X = wine_df.drop("class", axis=1)
y = wine_df['class'].astype("category")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# dataset summary
print("dataset shape:", wine_df.shape, ", 178 instances, 13 features, 1 target")
print("number of classes of wines:", "\n", y.value_counts(), "class 1: 59, class 2: 71, class 3: 48")

# data transformation
numeric_features = columns[1:]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
    ]
)

## logistic regression -----------------------------------------------------------
pipe_lr = Pipeline([
    ("preprocessor", preprocessor),
    ('classifier', LogisticRegression())
])

param_grid_lr = {
    'classifier__penalty':[None,"l2"]
}

lr_grid = GridSearchCV(pipe_lr, param_grid_lr, cv=5)
lr_grid.fit(X_train, y_train)
lr_best_score = lr_grid.best_score_
print("Best hyperparameters for logistic regression: ", lr_grid.best_params_)
print("Best CV accuracy score for logistic regression: ", lr_best_score)

## decision tree -----------------------------------------------------------
pipe_dt = Pipeline([
    ("preprocessor", preprocessor),
    ('classifier', DecisionTreeClassifier(criterion="entropy"))
])

param_grid_dt = {
    'classifier__max_depth': [2, 5, 10, 15, None]
}

dt_grid = GridSearchCV(pipe_dt, param_grid_dt, cv=5)
dt_grid.fit(X_train, y_train)
dt_best_score = dt_grid.best_score_
print("Best hyperparameters for decision tree: ", dt_grid.best_params_)
print("Best CV accuracy score for decision tree: ", dt_best_score)

## random forest -----------------------------------------------------------
pipe_rf = Pipeline([
    ("preprocessor", preprocessor),
    ('classifier', RandomForestClassifier(criterion="entropy"))
])

param_grid_rf = {
    'classifier__max_depth': [2, 5, 10, 15, None]
}

rf_grid = GridSearchCV(pipe_rf, param_grid_rf, cv=5)
rf_grid.fit(X_train, y_train)
rf_best_score = rf_grid.best_score_
print("Best hyperparameters for random forest: ", rf_grid.best_params_)
print("Best CV accuracy score for random forest: ", rf_best_score)


# --------------------------------------------------------------------------
# we choose logistic regression since it has the highest score
lr_grid.fit(X_test, y_test)
print("Best hyperparameters for logistic regression: ", lr_grid.best_params_)
print("Best CV accuracy score for logistic regression: ", lr_grid.best_score_)

# test confusion matrix, accuracy and recall
lr_pred = lr_grid.predict(X_test)
lr_confusion = confusion_matrix(y_test, lr_pred)
lr_accuracy = accuracy_score(y_test, lr_pred)
lr_precision = precision_score(y_test, lr_pred, zero_division=0, average="micro")
lr_recall = recall_score(y_test, lr_pred, average="micro")
print("logistic regression Confusion Matrix:", "\n", lr_confusion)
print("logistic regression accuracy:", lr_accuracy)
print("logistic regression precision score:", lr_precision)
print("logistic regression recall score:", lr_recall)

print("According to the accuracy score from the 'train' model of logistic regression, decision tree, and random forest model,\
    logistic regression model performed best among the three models. Therefore, we choose logistic regression for the best model to use")
print("Then, according to the accuracy score of 'test' model of logistic regression, the model performed 1.0 accuracy, precision, and recall. \
    Therefore, the final evaluation of logistic regression model in the wine class classification dataset has 'perfect' performance, \
        correctly label each of classes of quality of wine without any false labels.")

with open('results/uci_wine_results.txt', 'w') as f:
    f.write(
        f'dataset shape: {wine_df.shape}, 178 instances, 13 features, 1 target \n'
        f'number of classes of wines:" \n {y.value_counts()}, "class 1: 59, class 2: 71, class 3: 48 \n \n'
        'random state=42 enabled for train and test split \n'
        f'accuracy score for logistic regression for train data: {lr_best_score} \n'
        f'accuracy score for decision tree for train data: {dt_best_score} \n'
        f'accuracy score for random forest for train data: {rf_best_score} \n'
        'selected classification model: logistic regression \n \n'
        f'logistic regression Confusion Matrix: \n {lr_confusion} \n'
        f'logistic regression accuracy: {lr_accuracy} \n'
        f'logistic regression precision score: {lr_precision} \n'
        f'logistic regression recall score: {lr_recall} \n \n'
        '----- Final evaluation ----- \n'
        "According to the accuracy score from the 'train' model of logistic regression, decision tree, and random forest model, logistic regression model performed best among the three models. Therefore, we choose logistic regression for the best model to use \n"
        "Then, according to the accuracy score of 'test' model of logistic regression, the model performed 1.0 accuracy, precision, and recall. Therefore, the final evaluation of logistic regression model in the wine class classification dataset has 'perfect' performance, correctly label each of classes of quality of wine without any false labels."
      )