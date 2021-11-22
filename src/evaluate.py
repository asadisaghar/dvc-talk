import os
import sys
import yaml
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

train_path = sys.argv[1]
X_valid = pd.read_pickle(os.path.join(train_path, 'X_valid.pkl'))
y_valid = pd.read_pickle(os.path.join(train_path, 'y_valid.pkl'))

xg_reg = joblib.load(sys.argv[2])

y_pred = xg_reg.predict(X_valid)
rmse = np.sqrt(mean_squared_error(y_valid, y_pred))
r2 = r2_score(y_valid, y_pred)

scores_file = sys.argv[3]
metrics = {'rmse': rmse, 'r2': r2}
with open(scores_file, "w") as outfile:
    json.dump(metrics, outfile, indent=4)
    
preds_file = sys.argv[4]
y = pd.DataFrame()
y['y_true'] = y_valid
y['y_perd'] = y_pred
preds = y.to_dict('records')
with open(preds_file, "w") as outfile:
    json.dump(preds, outfile, indent=4)
    
