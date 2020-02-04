# coding=utf8
__author__ = 'wzw'
import pandas as pd
import numpy as np
import datetime
import os
import warnings
import pickle
warnings.filterwarnings("ignore")

class SelectDataMatrix:
    """
    """
    def __init__(self):
    	self.where = "Kdata"
    	self.path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]+'\\datapkl\\'+ self.where + "\\"

    def alterpath(self,where):
    	self.where = where


    def datekey(self):
    	with open(self.path  + "date.pkl", 'rb') as f:
    		self.date = pd.DataFrame(pickle.load(f))
    		self.date =["date"] 

    def codekey(self,ind):
    	path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]+'\\datapkl\\'+ ind[1] + "\\"
    	fl = path + ind[0] +".pkl"
    	with open(fl, 'rb') as f:
    		indser = pd.DataFrame(pickle.load(f))
    		indser.columns =[ind[0]] 
    	return indser    	
    	
    def get(self,ind):
    	path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]+'\\datapkl\\'+ ind[1] + "\\"
    	fl = path + ind[0] +".pkl"
    	with open(fl, 'rb') as f:
    		indser = pd.DataFrame(pickle.load(f))
    		indser.columns =[ind[0]] 
    	return np.array(indser.values.tolist()).flatten()


if __name__=='__main__':
	S = SelectDataMatrix()
	inds = ["close", "open"]
	S.getoneind(inds)
	S.ppp()