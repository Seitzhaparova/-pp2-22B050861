import json
import pandas as pd

with open('sample_data.json', 'r') as fl:
    data = json.load(fl)

dl = []

for item in data['imdata']:
    if 'l1PhysIf' in item:
        l1PhysIf_dct = item['l1PhysIf']['attributes']
        dnV = l1PhysIf_dct.get('dn')
        descrV = l1PhysIf_dct.get('descr')
        speedV = l1PhysIf_dct.get('speed')
        mtuV = l1PhysIf_dct.get('mtu')
        dl.append({'DN': dnV, 'Description': descrV, 'Speed': speedV, 'MTU': mtuV})

df = pd.DataFrame(dl)
print(df)