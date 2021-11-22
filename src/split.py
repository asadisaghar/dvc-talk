import os
import sys
import yaml
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

params = yaml.safe_load(open('params.yaml'))['split']
data = pd.read_pickle(sys.argv[1])
cat_feats = yaml.safe_load(open(sys.argv[2]))
num_feats = yaml.safe_load(open(sys.argv[3]))

X = data.loc[:, data.columns != 'Y']
y = data.loc[:, 'Y']
X = pd.get_dummies(
    X, 
    prefix=cat_feats, 
    columns=cat_feats, 
    dummy_na=True, 
    drop_first=False
    )
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, 
    test_size=params['test_size'], 
    random_state=params['random_state']
    ) 

scaler = MinMaxScaler()
scaler.fit(X_train[num_feats])
X_train[num_feats] = scaler.transform(X_train[num_feats])
X_valid[num_feats] = scaler.transform(X_valid[num_feats])

if not os.path.isdir(params['out_dir']):
    os.makedirs(params['out_dir'])
X_train.to_pickle(os.path.join(params['out_dir'], 'X_train.pkl'))
y_train.to_pickle(os.path.join(params['out_dir'], 'y_train.pkl'))

X_valid.to_pickle(os.path.join(params['out_dir'], 'X_valid.pkl'))
y_valid.to_pickle(os.path.join(params['out_dir'], 'y_valid.pkl'))

