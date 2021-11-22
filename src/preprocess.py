import sys
import yaml
import pandas as pd 

params = yaml.safe_load(open('params.yaml'))['preprocess']

data = pd.read_csv(sys.argv[1], delimiter=";")
if params['features'] is not None:
    features = params['features']
    features.append('Y')
    data = data[features].copy()
    print('Keeping these features:', features)
else:
    features = data.columns.tolist()
    print('Keeping all the features')

if params['rows'] is not None:
    if params['rows'] < len(data):
        data = data.sample(params['rows'])
        print('Keeping {} sampleds', format(params['rows']))
    else:
        print('Keeping all the rows')
    
cat_feats = []
for feat in features:
    if data[feat].nunique()<10:
        cat_feats.append(feat)
yaml.safe_dump(cat_feats, open('data/cat_feats.yaml', 'w'))
num_feats = list(set(features) - set(cat_feats))
num_feats.remove('Y')
yaml.safe_dump(num_feats, open('data/num_feats.yaml', 'w'))
print('Categorical features: ', cat_feats)
print('Numerical features:', num_feats)

data.to_pickle('data/preprocessed.pkl')