# coding=utf-8
import pandas as pd
from geojson import Feature,Point,FeatureCollection,dump
COL_NAMES = ['Datetime','Lat','Lon','Intensity','Gradient','Error','Mode','Province','City','County']
df = pd.read_csv('static/tmp/thunder.csv',header=None,names=COL_NAMES,delim_whitespace=True)

features = list()
for idx,row in df.iterrows():
    features.append(Feature(geometry=Point(coordinates=[row['Lon'],row['Lat']])))

collections = FeatureCollection(features)
with open('test.geojson','w') as fp:
    dump(collections,fp)