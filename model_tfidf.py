from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd 
from preprocess import DataSource
from utils import util
from sklearn.feature_extraction.text import CountVectorizer
from pyvi import ViTokenizer, ViPosTagger

class Dict_Tfidf():
	def __init__(self,path):
		self.path = path
	
	def create_dict_tfidf(self):
		ds = DataSource()
		dict_data = pd.DataFrame(ds.load_data(self.path, is_train=True)).review
		dict_data = dict_data.tolist()
		Util = util()
		A = []
		for i in range(len(dict_data)):
			text = dict_data[i]
			text = Util.text_util_final(text)
			# text = ViPosTagger.postagging(ViTokenizer.tokenize(text))[1]
			# sent = ""
			# for token in text:
			# 	sent += token + " "
			A.append(text)

		# ngram_range cũng chính là phần tách thành các unigrams, bigrams, trigrams
		vectorizer = TfidfVectorizer(max_features=100000,ngram_range=(1, 3), sublinear_tf=True)
		vectorizer.fit_transform(A)
		return vectorizer

if __name__ == '__main__':
	DT = Dict_Tfidf("./data/train.crash")
	DT.create_dict_tfidf()