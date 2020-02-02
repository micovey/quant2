# coding=utf8
__author__ = 'wzw'
import pandas as pd
import numpy as np
import datetime
import os
#import CalModel as CM
import warnings
import pickle
warnings.filterwarnings("ignore")
# class Address:
# 	def __init__(self):	
# 		self.root = []
# 	# def __str__(self):
# 	# 	msg=""
# 	# 	for i in self.dirs:
# 	# 		msg += i
# 	# 	return msg
# 	def getp(self):
# 		for root, dirs, files in os.walk(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + '\\datapkl\\'):
# 			self.root.append(root)
# 		self.root.pop(0)
# 		for p in self.root:
# 			for root, dirs, files in os.walk(p):
# 					pass
# 			print(files)

# 		print(self.root) 
# # 		path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + '\\datapkl\\' + where
# #         print(path)
# #         for root, dirs, files in os.walk(path):
# #             pass

# if 1 in lista:
#     print('1 在列表lista中')

# 		self.field = {
# 		"date":
# 		}

	# def pr(self):
	# 	where = "Kdata"
	# 	path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]+'\\datapkl\\'+ where + "\\date.pkl"
	# #	print(path)

	# A = Address()
	# A.getp()

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



    	# self.codekey()
    	# for ind in inds:
	    # 	fl = self.path + ind +".pkl"
	    # 	with open(fl, 'rb') as f:
	    # 		indser = pd.DataFrame(pickle.load(f))
	    # 		indser.columns =[ind] 
	    # 	self.mat = pd.concat([self.mat,indser],axis=1).reset_index(drop=True)

if __name__=='__main__':
	S = SelectDataMatrix()
	inds = ["close", "open"]
	S.getoneind(inds)
	S.ppp()



#     	con = sql.connect(host="localhost", user="root", passwd=self.pword,db=self.dbname,port=3306)
#     	cur = con.cursor(cursorclass=sql.cursors.DictCursor)
#     	col = ",".join(ind)
#     	sql_ = 'SELECT {} FROM {};'.format(col,tablename)           # MODIFY pubDate DATE PRIMARY KEY;'
#     	cur.execute(sql_)
#     	datmax = cur.fetchall()
#     	datmax = pd.DataFrame(datmax)
#     	self.datmax = datmax
    	

# if __name__=='__main__':

# 	# code = pd.read_csv(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + "\DownloadData\idcode.csv", encoding='utf-8')
# 	# for id in code["idcode"]:
# 	num = 20
# 	ind=["date","code","pctChg","preclose","close","amount"]
# 	S = SelectDataMatrix("root","quant")
# 	S.getdatamat("kdata",ind)
# 	print(S.datmax)
# 	del S
# 	# if (len(S.datmax) > num):
# 	# 	Cal = CM.CalMethod(S.datmax)
# 	# 	cor = Cal.Meanoneid("close",num)
# 	# 	print(id)










# x = np.array([1,2,3,6,7,9,7,4,2,7,5,3,5,7,2,1,5,6,8,0,-1,4,6,8,2,12,35,7,9,21,23,7,3,1,4,6])
# y = 1/np.sqrt(np.sqrt(1/np.log(x+1.1)+10))
# z = np.corrcoef(x,y)
# print(x)
# print(y)
# print(z)