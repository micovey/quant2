# coding=utf8
__author__ = 'wzw'
import pandas as pd
import numpy as np
import datetime
import os
import SelectData as SD
import math
import ColName as CN
class CalMethod:
 	def __init__(self):
 		self.SLD = SD.SelectDataMatrix()
 		self.code = []
 		self.date = []
 		self.j=0
 	def __checkcode(self,col):
 		col = pd.DataFrame(col)		
 		l = len(col)
 		if len(self.code) == l:
 			pass
 		else:
	 		if l > 2000000:
	 			self.code = self.SLD.codekey(["code","Kdata"])	
	 		else:
	 			self.code = self.SLD.codekey(["code","Kindex"])
	 	col = pd.concat([self.code,col],axis=1).reset_index(drop=True) 	
	 	grouped = col.groupby('code')
	 	return grouped
 	def __checkdate(self,col):
 		col = pd.DataFrame(col)		
 		l = len(col)
 		if len(self.date) == l:
 			pass
 		else:
	 		if l > 2000000:
	 			self.date = self.SLD.codekey(["date","Kdata"])	
	 		else:
	 			self.date = self.SLD.codekey(["date","Kindex"])
	 	col = pd.concat([self.date,col],axis=1).reset_index(drop=True) 	
	 	grouped = col.groupby('date')
	 	return grouped


 	def __checkcode2(self,col1,col2):
 		col1 = pd.DataFrame(col1)
 		col2 = pd.DataFrame(col2)
 		l = len(col1)
 		if len(self.code) == l:
 			pass
 		else:
	 		if l > 2000000:
	 			self.code = self.SLD.codekey(["code","Kdata"])	
	 		else:
	 			self.code = self.SLD.codekey(["code","Kindex"])
	 	col = pd.concat([self.code,col1,col2],axis=1).reset_index(drop=True)
	 	grouped = col.groupby('code')
	 	return grouped
 	def __shift(self,num,g):
 		g.iloc[:,1] = g.iloc[:,1].shift(periods=num)
 		return g
 	def __diff(self,num,g):
 		x = self.__shift(g.iloc[:,1],num)
 		g = g.iloc[:,1] - x
 		return g
 	def __sum(self,num,g): 
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).sum()
 		return g
 	def __mean(self,num,g): 
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).mean()
 		return g
 	def __median(self,num,g): 
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).mean()
 		return g
 	def __std(self,num,g):
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).std()
 		return g
 	def __var(self,num,g):
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).var()
 		return g 	
 	def __skew(self,num,g):
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).skew()
 		return g
 	def __kurt(self,num,g):
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).kurt()
 		return g 	
 	def __min(self,num,g):
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).min()
 		return g 	
 	def __max(self,num,g):
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).max()
 		return g
 	def __cutroll(self,num,sig,g):
 		self.j +=1
 		def cutroll_(x,num):
 			x = np.array(x)
 			minst = np.mean(x) - sig * np.std(x)
 			maxst = np.mean(x) + sig * np.std(x)
 			if x[-1] > maxst:
 				x[-1] = maxst
 			elif x[-1] <minst:
 				x[-1] =  minst
 			else:
 				pass
 			return x[-1]
 		g.iloc[:,1] = g.iloc[:,1].rolling(window=num).apply(lambda x: cutroll_(x,sig))
 		return g		
 	def __cut(self,sig,g):
 		g = np.array(g.iloc[:,1])
 		minst = np.mean(g) - sig * np.std(g)
 		maxst = np.mean(g) + sig * np.std(g)
 		g = np.clip(g,minst,maxst)
 		return pd.DataFrame(g)	
 	def __corr(self,num,g):
 		corr = g.iloc[:,1].rolling(window=num).corr(g.iloc[:,2])
 		corr = corr.fillna(0)	
 		return corr
 	def __reg(self,num,g):	
 		mx = g.iloc[:,1].rolling(window=num).mean() 
 		my = g.iloc[:,2].rolling(window=num).mean() 
 		upsum = (g.iloc[:,1] * g.iloc[:,2]).rolling(window=num).sum() - num * mx * my
 		downsum = (g.iloc[:,1] ** 2).rolling(window=num).sum() - num * mx**2
 		beta = upsum / downsum
 		alpha = my - beta * mx
 		sigma = ((g.iloc[:,2] - beta * g.iloc[:,1])**2).rolling(window=num).sum()
 		g = pd.concat([alpha,beta,sigma],axis=1).reset_index(drop=True)
 		return g
 	def __ncskew(self,num,g):##速度太慢
 		def ncskew_(x,num):
 			x = np.array(x)
 			sum3 =np.sum(x**3)
 			sum2 =np.sum(x**2)
 			up = (-num) * ((num-1) ** 1.5) * sum3
 			down = (num-1) * (num-2) * (sum2 ** 1.5)
 			g1 = up / down
 			if down == 0:
 				g1 = np.nan
 			return g1
 		g = g.iloc[:,1].rolling(window=num).apply(lambda x: ncskew_(x,num))
 		return g		
 	def __duvol(self,num,g):##速度太慢
 		def duvol_(x,num):
 			x = np.array(x)
 			aver = np.mean(x)
 			dum = 0
 			for x1 in x:
 				if x1 > aver:
 					upret2 = x1 * x1
 					dum += 1
 				else:
 					downret2 = x1 * x1
 			if (dum == 0 or dum == num):
 				g1 = np.nan
 			else:
	 			up = (dum-1) * np.sum(downret2)
	 			down = (num - dum-1) * np.sum(upret2)
	 			g1 = up / down
	 			if down == 0:
	 				g1 = np.nan		
 			return np.log(g1)
 		g = g.iloc[:,1].rolling(window=num).apply(lambda x: duvol_(x,num))
 		return g
 	def __hurst(self,num,data):##速度太慢
 		self.j +=1
 		print(self.j)
 		def reg_(x,y):
 			x = np.array(x)
 			y = np.array(y)
 			upsum = np.sum(x * y) - len(x) * np.mean(x) * np.mean(y)
 			downsum = np.sum(x ** 2)- len(x) * np.mean(x)**2
 			beta = upsum / downsum
 			return beta  		
 		def hurst_(data):
	 		pannel_num = 4
	 		ARS =[]
	 		lag =[]
	 		data = np.array(data).flatten()
	 		for i in range(pannel_num):
	 			size = np.size(data) // (2 ** i)
	 			lag.append(size)
	 			panel = {}
	 			for sub_pannel_num in range((2 ** i)):
	 				panel[sub_pannel_num] = data[sub_pannel_num*size:(sub_pannel_num+1)*size]
	 			panel = pd.DataFrame(panel)
	 			Dev = (panel - panel.mean()).cumsum()
	 			RS = (Dev.max() - Dev.min())/panel.std()
	 			ARS.append(RS.mean())
	 		return reg_(np.log10(lag), np.log10(ARS))
	 	data = data.iloc[:,1].rolling(window=num).apply(lambda x: hurst_(x))
	 	return data

 	def Shift(self,col,num):	# 向前移动num天
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__shift(num,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def Diff(self,col,num):	# 过去 num 天差额
 		x = self.Shift(col,num)
 		col = col - np.array(x).flatten()
 		return col

 	def Sum(self,col,num):	# 过去 num 天之和
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__sum(num,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].tolist()).flatten()

 	def Mean(self,col,num):	# 过去 num 天均值
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__mean(num,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def Median(self,col,num):	# 过去 num 天均值
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__median(num,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def Std(self,col,num):	# 过去 num 天标准差
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__std(num,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def Var(self,col,num):  # 过去 num 天方差
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__var(num,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def Skew(self,col,num):	# 过去 num 天偏度
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__skew(num,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def Kurt(self,col,num):	# 过去 num 天峰度
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__kurt(num,x)).reset_index(drop=True)
 		return gnp.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def Min(self,col,num):	# 过去 num 天最小值
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__min(num,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def Max(self,col,num):	# 过去 num 天最大值
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__max(num,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def CutRoll(self,col,num,sig): # 每num天，按照sig个标准差截尾
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__cutroll(num,sig,x)).reset_index(drop=True)
 		return np.array(grouped.iloc[:,1].values.tolist()).flatten()	

 	def Cut(self,col,sig):  # 直接按照sig个标准差截尾
 		grouped = self.__checkcode(col)
 		grouped = np.array(grouped.apply(lambda x: self.__cut(sig,x)).reset_index(drop=True).values.tolist()) 
 		return grouped.flatten()

 	def Corr(self,col1,col2,num): # 过去 num 天相关性，双变量
 		grouped = self.__checkcode2(col1,col2)
 		grouped = grouped.apply(lambda x: self.__corr(num,x)).reset_index(drop=True)
 		return  np.array(grouped.values.tolist()).flatten()

 	def Reg(self,col1,col2,num): # 过去 num 天回归系数，双变量 col1为x, col2为y, 顺序为 alpha beta sigma（残差平方和）
 		grouped = self.__checkcode2(col1,col2)
 		grouped = grouped.apply(lambda x: self.__reg(num,x)).reset_index(drop=True)
 		alpha = np.array(grouped.iloc[:,0].values.tolist()).flatten()
 		beta = np.array(grouped.iloc[:,1].values.tolist()).flatten()
 		sigma = np.array(grouped.iloc[:,2].values.tolist()).flatten()
 		return alpha, beta, sigma

 	def Ncskew(self,col,num): # 过去 num 天崩盘风险
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__ncskew(num,x)).reset_index(drop=True)
 		return np.array(grouped.values.tolist()).flatten()

 	def Duvol(self,col,num): # 过去 num 天崩盘风险
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__duvol(num,x)).reset_index(drop=True)
 		return np.array(grouped.values.tolist()).flatten()

 	def Hurst(self,col,num): # 长记忆性指数
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: self.__hurst(num,x)).reset_index(drop=True)
 		return np.array(grouped.values.tolist()).flatten()

 	def Ewm(self,col,num): # 加权
 		grouped = self.__checkcode(col)
 		grouped = grouped.apply(lambda x: x.iloc[:,1].ewm(span=num,ignore_na=True).mean()).reset_index(drop=True)
 		return np.array(grouped.values.tolist()).flatten()
 	"""
 	截面指标
 	"""
 	def Rank(self,col,pct= False):
 		grouped = self.__checkdate(col)
 		grouped = grouped.apply(lambda x: x.iloc[:,1].rank(na_option='bottom', pct=pct, ascending=True)).reset_index(drop=True)
 		return grouped.values.tolist()





if __name__=='__main__':
	C=CN.ColName() # 对应文件名
	SLD = SD.SelectDataMatrix() # 需要的数据框，是一个可以groupby的dataframe
	Cal = CalMethod()#寻找上面对应的计算方法
	ret = SLD.get(C.pctChg)
	amt = SLD.get(C.amount)
	cor = Cal.Corr(amt,ret,30)
	print(pd.DataFrame(cor))#一个简单的结果










