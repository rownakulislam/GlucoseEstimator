import json
import numpy as np
import pickle

with open('./artifacts/columns.json', 'r') as f:
    __data_columns = json.load(f)['data_columns']

with open('./artifacts/project_svm_model.pickle','rb') as f:
    __model=pickle.load(f)


def get_estimated_glucose(age,sbp,dbp,pulse,bmi,weight,f,m):
    x=np.zeros(8)
    x[0]=age
    x[1]=sbp
    x[2]=dbp
    x[3]=pulse
    x[4]=bmi
    x[5]=weight
    x[6] = f
    x[7] = m
    print(__model.predict([x]))
    return round(__model.predict([x])[0],2)

def get_column_names():
    return __data_columns
def load_saved_artifacts():
    print("Loading saved artifacts: ")
    print("loading artifacts is done")

if __name__=='__main__':
    load_saved_artifacts()
    print(get_column_names())
    print(get_estimated_glucose(40,110,60,90,23.4,58.641935,0,1));
    # print(get_estimated_glucose(6,72,35,33.6,50,30.5))