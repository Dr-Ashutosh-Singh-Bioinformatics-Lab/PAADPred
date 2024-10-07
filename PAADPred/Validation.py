# PAAD/Validation.py

import os
import pandas as pd
import joblib

def predict(df, model_type='svc'):
    # List of selected genes
    selected_genes = ['CACNG3', 'ZIC2', 'SPI1', 'SNX10', 'FXYD3', 'TDRD1', 'HMOX1', 'PDYN', 'HCK', 'FAM83D', 'JPH1', 'MAN2B1', 'TUBB4A', 'LILRB1', 'CD33', 'KLF1', 'ABI3', 'GPRC5D', 'NCF2', 'TNFAIP3', 'SPDEF', 'SIGLEC9', 'PYY', 'DDC', 'MYBPH', 'PRAM1', 'ERN2', 'SOX3', 'NPL', 'GYPC', 'RNF144B', 'FHDC1', 'ARRB2', 'MYO1F', 'ABCA12', 'LGSN', 'GGTLC1', 'PTPRO', 'RASGRP3', 'ASZ1', 'ALAS2', 'C1QC', 'CYP3A4', 'NPY5R', 'PPP1R14D', 'LAIR1', 'SIGLEC7', 'OR4D5', 'FPR1', 'ADRA1D', 'CLEC12A', 'MAB21L4', 'XKR3', 'C1QB', 'FAM166C', 'PXT1', 'MKRN3', 'CFAP65', 'EPHB3', 'ACSM5', 'ADAP2', 'STAC3', 'PRSS38', 'CD300LF', 'ARAP1', 'IFNA2', 'KEL', 'FCGR3A', 'PSG5', 'PSG3', 'APOC4-APOC2', 'AC013470.2', 'HLA-DQA2', 'MTRNR2L10', 'AC023055.1', 'GRIN2B']
    # Select features from dataframe
    df_selected = df[selected_genes]
    
    # Construct model path
    model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_type.lower()}.pkl')
    
    # Check if model file exists
    if not os.path.exists(model_path):
        raise ValueError(f"Model '{model_type}' not found. Ensure the model file exists at {model_path}.")
    
    # Load the model
    model = joblib.load(model_path)
    
    # Make predictions
    y_pred = model.predict(df_selected)
    
    # Add predictions to dataframe
    df['Prediction'] = ['Cancer' if pred == 1 else 'Normal' for pred in y_pred]
    
    # Save predictions to CSV file
    df.to_csv('predictions.csv', index=False)
    
    # Print diagnosis
    count_cancer = y_pred.sum()
    count_normal = len(y_pred) - count_cancer
    percentage_cancer = count_cancer / len(y_pred)
    percentage_normal = count_normal / len(y_pred)
    
    if percentage_cancer > 0.6:
        print(f"PAAD patient detected, {percentage_cancer*100:.2f}%")
    else:
        print(f"Normal patient detected, {percentage_normal*100:.2f}%")
