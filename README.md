# PAADPred: A Tool for Identification of Pancreatic Cancer using Machine Learning.
Pancreatic adenocarcinoma is the most common form of pancreatic cancer, originating in the glandular cells of the pancreas. Biomarkers are essential for its early detection, as symptoms often appear late. Identifying reliable biomarkers improves diagnosis, guides treatment decisions, and enhances prognosis, ultimately increasing the chances of better patient outcomes. Biomarkers are pivotal in this regard, providing noninvasive means for early detection, facilitating prompt treatment initiation, and potentially boosting survival rates. Hence, the recognition and validation of biomarkers are of primary importance in effectively addressing pancreatic cancer.


## Introduction

PAADPred is an innovative solution for identifying pancreatic adenocarcinoma through transcriptomic profiling. By leveraging advanced machine learning algorithms, this cutting-edge technology analyzes tissue biomarkers to deliver highly accurate prognoses for pancreatic cancer.

Furthermore, the integration of machine learning allows for continuous refinement of the predictive model’s accuracy as more data is gathered, enhancing its reliability and effectiveness over time. PAADPred represents a significant breakthrough in the early detection of pancreatic adenocarcinoma, potentially leading to earlier interventions and improved patient outcomes.

To further strengthen our approach, we selected 76 features using a range of Feature Selection Methods. These include the Fast Correlation-Based Filter Method (FCBF), Spike and Slab ("spikeslab"), Univariate statistical tests (F-test), and wrapper methods like Boruta and Recursive Feature Elimination (RFE). Additionally, we employed embedded methods such as XGBoost, SVC linear with the SelectFromModel class from scikit-learn, Random Forest, Extra Trees with Feature Importance, and LASSO (a regularization-based embedded method). By combining Filter, Wrapper, and Embedded feature selection techniques, we used an ensemble approach to identify features present in at least five methods. These 76 features show potential as biomarkers for classifying and predicting normal versus cancerous patients.




Installation and Usage:

You can install the package using the following command:


    git clone https://github.com/GITractCancer/PAADPred.git
    cd PAADPred



### Predict using PAADPred

    import pandas as pd
    from PAADPred import predict

    df = pd.read_csv("path/to/your/data.csv")

    predict(df, model_type='svc')

    
Specify the model type you want to use Models


## Models

The following classifiers are supported:

    svc
    rf
    ab
    xgb
    dt
    et
    lr
    gnb
    knn
    mlp
