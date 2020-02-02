# coding=utf8
__author__ = 'wzw'

import os
import configparser as cp

class Import:
# os模块，寻找文件位置
fp = os.path.realpath(__file__)#当前文件路径
# fp: "D:\Quant\ImportData\ReadData.py"
				#thisPath, moduleFile = os.path.split(os.path.realpath(__file__))
up = os.path.split(os.path.split(fp)[0])[0]#D:\Quant
# up: "D:\Quant"
ReadPath = up + '\DataPath\Path.ini'#D:\Quant\DataPath\Path.ini
conf = cp.ConfigParser() 
conf.read(ReadPath)
sections = conf.sections()
Path = conf.get('data', 'Path')#D:\Quant\D:\Quant\data\
print (fp,up,ReadPath,Path)
#输出结果