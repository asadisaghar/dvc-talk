import os
import sys
import yaml
import joblib
import pandas as pd
import xgboost as xgb

params = yaml.safe_load(open('params.yaml'))['train']
train_path = sys.argv[1]

X_train = pd.read_pickle(os.path.join(train_path, 'X_train.pkl'))
y_train = pd.read_pickle(os.path.join(train_path, 'y_train.pkl'))

xg_reg = xgb.XGBRegressor(objective='reg:squarederror', 
                          colsample_bytree=params['colsample_bytree'], 
                          learning_rate=params['learning_rate'],
                          max_depth=params['max_depth'], 
                          n_estimators = params['n_estimators']
                          )
xg_reg.fit(
    X_train, y_train,
    verbose=False
    )

joblib.dump(xg_reg, 'model.joblib')