# is477-fall2023-final-project
Public repository for IS477 Fall 2023 final project

## Overview
- **Purpose**: is477-fall2023-final-project is Github repository for the final project of IS 477 Data Management class. The project is about creating the pipeline or the entire process of data management, such as acquisition of data, check integrity of data, data analysis, preservation, legal concerns, and reproduce of data and analysis. 
- **Overall project requirements**: The project requires basic installation of GitHub, Docker, VScode, and GitHub accounts with repositories for the final project of IS 477. 
- **Dataset**: The dataset used for this project is from UC Irvine Machine Learning Repository (https://archive.ics.uci.edu/), and the dataset is Wine dataset (https://doi.org/10.24432/C5PC7J). Wine dataset contains total 14 columns that consist of 13 features and 1 target variable for classification purpose. The dataset has total 178 rows, or instances. 
- **Analysis**: The purpose of the analysis is figuring out which machine learning classification model showing a best classification of quality of wine that based on 3 classes. The dataframe splitted into target variable (y) and features (X), and then splitted more into train X and y for select classfication model based on metrics scores and test X and y for give final evaluation on the selected classfication model. All models are standard scaled and Grid Searched with 5 fold corss validations to figuring out best parameters with less overfitting for each models.


## Contributions

## Analysis
1. From the applying the train dataset, Logistic Regression showed the best accuracy score: 1. Therefore, Logistic Regression is selected for the final application for classification.
2. Then, the selected model, Logistic Regression is fitted with test X and y for the final evaluation of the model. To evaluate the model with slightly more detailed, confusion matrix with metrics like accuracy, precision, and recall used. Logistic Regression showed all correct, 100% accuracy, precision, and recall with no negatives or error in confusion matrix. 
- **Result**: Logistic Regression showed the best performance to classifying wine quality class according to the analysis, compare to Decision Tree and Random Forest. However, since the dataset contains only 178 instances, considering this analysis as no more than performance purposes and may be further works needed for applying to the work place.

## Workflow

## Reproducing
- All the code in the program need the python environment of Python 3.11.1
- Download the adult.zip from https://doi.org/10.24432/C5PC7J
- Use Logistic Regression mofel to fit the data
- Compare the results between different parameters

## License
- Creative Commons CCZero (CC0-1.0) for the license.
- Characteristic: No Copyright, Global Applicability, Freedom to Use.
- It is a very good license to my project, because it provides the neccessary part of it


## References
- Aeberhard,Stefan and Forina,M.. (1991). Wine. UCI Machine Learning Repository. https://doi.org/10.24432/C5PC7J.
- https://cs307.org/notes/week-08/week-08.html
- https://cs307.org/notes/week-09/week-09.html
- https://cs307.org/lab/lab-05/lab-05.html
- https://cs307.org/lab/lab-06/lab-06.html
- https://cs307.org/lab/lab-08/lab-08.html