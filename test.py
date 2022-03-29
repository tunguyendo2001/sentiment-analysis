from model_tfidf import Dict_Tfidf
# from sklearn.externals import joblib
import joblib
import exception
import argparse
from utils import util
from preprocess import DataSource
import pandas as pd
import numpy as np
PATH = "./data/train.crash"

def create_tfidf_vector(path):
    dict_tfidf = Dict_Tfidf(PATH)
    vectorizer = dict_tfidf.create_dict_tfidf()

    #load du lieu
    ds = DataSource()
    test_data = pd.DataFrame(ds.load_data(path, is_train=False))
    x_test = test_data.review
    # chuan hoa lai du lieu
    x_test = x_test.tolist()
    Util = util()
    A = []
    for i in range(len(x_test)):
        text = x_test[i]
        text = Util.text_util_final(text)
        A.append(text)

    #Chuyen ve vector tfidf    
    x_test_tfidf = vectorizer.transform(A)
    return x_test_tfidf

def testing():
    x_test_tfidf = create_tfidf_vector(PATH)
    model= joblib.load('./models/best_model.pkl')
    label = np.zeros(shape=(x_test_tfidf.shape[0], 1))
    for i in range(x_test_tfidf.shape[0]):
        if i == 2:
            print(x_test_tfidf[i])
            print(model.predict(x_test_tfidf[i]))

if __name__ == '__main__':
    testing()