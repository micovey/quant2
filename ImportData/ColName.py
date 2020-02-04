# coding=utf8
__author__ = 'wzw'
class ColName:
	def __init__(self):
		self.pctChg = ["pctChg","Kdata"]
		self.close = ["close","Kdata"]
		self.open = ["open","Kdata"]
		self.high = ["close","Kdata"]
		self.low = ["close","Kdata"]
		self.preclose = ["preclose","Kdata"]
		self.volume = ["volume","Kdata"]
		self.amount = ["amount","Kdata"]
		self.turn = ["turn","Kdata"]
		self.tradestatus = ["tradestatus","Kdata"]
		self.peTTM = ["peTTM","Kdata"]
		self.pbMRQ = ["pbMRQ","Kdata"]
		self.psTTM = ["psTTM","Kdata"]
		self.pcfNcfTTM = ["pcfNcfTTM","Kdata"]
		self.isST = ["isST","Kdata"]
		"""
        date:交易所行情日期  code:证券代码   open:开盘价 high:最高价 low:最低价 close:收盘价 preclose:前收盘价 volume:成交量（股） amount:成交额（元） adjustflag  复权状态(1：后复权， 2：前复权，3：不复权）    
        turn :换手率 [指定交易日的成交量(股)/指定交易日的股票的流通股总股数(股)]*100%  tradestatus:交易状态(1：正常交易 0：停牌）   pctChg:涨跌幅（百分比）    
        日涨跌幅=[(指定交易日的收盘价-指定交易日前收盘价)/指定交易日前收盘价]*100%
        peTTM   滚动市盈率   (指定交易日的股票收盘价/指定交易日的每股盈余TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/归属母公司股东净利润TTM
        pbMRQ   市净率 (指定交易日的股票收盘价/指定交易日的每股净资产)=总市值/(最近披露的归属母公司股东的权益-其他权益工具)
        psTTM   滚动市销率   (指定交易日的股票收盘价/指定交易日的每股销售额)=(指定交易日的股票收盘价*截至当日公司总股本)/营业总收入TTM
        pcfNcfTTM   滚动市现率   (指定交易日的股票收盘价/指定交易日的每股现金流TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/现金以及现金等价物净增加额TTM
        isST    是否ST股，1是，0否

        """
class GroupName:
		def __init__(self,names):
			self.type = 0
			if names == "close":
				self.type = ["date","code","close","pctChg"]
			if names == "shares":
				self.type = ["date","code","turn","volume","pctChg"]

