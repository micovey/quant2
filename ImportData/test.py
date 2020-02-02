# coding=utf8
__author__ = 'wzw'
import pandas as pd
import numpy as np
import datetime
import os
import sys
import math
sys.path.append(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]+"\\ImportData\\") 
sys.path.append(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]+"\\StoreFactor\\") 
import SelectData as SD
import ColName as CN
import CalModel as CM
import pickle
import matplotlib.pyplot as plt
class WriteFactor:
    def __init__(self,fctname):	
    	module = __import__(fctname)
    	
    	self.path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + "\\Fctvalue\\{}.pkl".format(fctname)
    	self.Factor = module.CalFactor()
    	self.__writefctsore()

    def __writefctsore(self):
    	output = open(self.path, 'wb')
    	pickle.dump(self.Factor.fct, output)
    	output.close() 

    def __del__(self):
    	print("已储存因子计算值至==>"+self.path)   


class Calret():
    def __init__(self,fctname):
    	# self.Cal = CM.CalMethod()
    	self.C = CN.ColName()
    	self.SLD = SD.SelectDataMatrix()
    	self.path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + "\\Fctvalue\\{}.pkl".format(fctname)
    	self.__preparemat()
    	
    def __weight(self,x):
    	n = x["close"]
    	weight = n /n.sum()
    	x["ret"] = x["pctChg"] * weight
    	#print(x["pctChg"] )
    	return x["ret"].sum()/100+1

    def __preparemat(self):
      	with open(self.path, 'rb') as f:
      		fct = pickle.load(f)
      	fct = pd.DataFrame(fct)
      	fct.columns =["fct"] 
      	code = self.SLD.codekey(["code","Kdata"])
      	date = self.SLD.codekey(["date","Kdata"])
      	pctChg = self.SLD.codekey(["pctChg","Kdata"])
      	close = self.SLD.codekey(["close","Kdata"])
      #	turn = self.SLD.codekey(["turn","Kdata"])
      #	volume = self.SLD.codekey(["volume","Kdata"])
      	self.mat = pd.concat([code,date,fct,pctChg,close],axis=1).reset_index(drop=True)
     # 	self.mat = self.mat.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
      	self.mat[["pctChg","close"]] = self.mat.groupby('code', as_index=False).apply(lambda x: x[["pctChg","close"]].shift(periods=-1)).reset_index(drop=True)
      	self.mat = self.mat.sort_index(by=['date','fct'],ascending=[True,False]).groupby('date', as_index=False).head(300)
      	self.mat = self.mat.groupby('date', as_index=True).apply(lambda x: self.__weight(x))#
      	self.mat.drop(self.mat.index[0:100])
      	self.mat =self.mat.cumprod()
      #	self.mat.to_csv("D:\\Quant\\1.csv", header=True,index=False)##输出  	
   
      	self.mat.plot()
      	plt.show()
	 			
	 	
if __name__=='__main__':
	# x = pd.DataFrame([12,2,3,4,5,6,7])
	# print(x + 1)
  #  W = WriteFactor("hurst")
    C = Calret("duvol")
