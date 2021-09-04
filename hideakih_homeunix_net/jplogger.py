#!/usr/bin/python

import sys
from logging import getLogger, Formatter, StreamHandler, FileHandler, DEBUG, INFO, WARNING, ERROR, CRITICAL

class jplogger():
	""" serve log method """
		
	debug = DEBUG
	info = INFO
	notice = 25
	warning = WARNING
	error = ERROR
	critical = CRITICAL

	# constructor
	'''
	def __init__(self):
		self.logger = getLogger(__name__)
		self.__formatter__ = Formatter(
			'%(asctime)s %(levelname)s %(message)s',
			'%Y/%m/%d %H:%M:%S')
		self.logger.setLevel(jplogger.debug)
		_shandler = StreamHandler()
		_shandler.setFormatter(self.__formatter__)
		_shandler.setLevel(jplogger.info)
		self.logger.addHandler(_shandler)
	'''
	
	def __init__(self, severity):
		self.logger = getLogger(__name__)
		self.severity = severity
		self.__formatter__ = Formatter(
			'%(asctime)s %(levelname)s %(message)s',
			'%Y/%m/%d %H:%M:%S')
		self.logger.setLevel(self.severity)
		self.handlers = {}
	#
	
	def addStdOutHandler(self, handler, severity):
		if handler in self.handlers.keys():
			self.logError('指定のハンドラー名は既に登録されています。登録は行いません')
			return False
		#
		
		_handler = StreamHandler(stream=sys.stdout)
		_handler.setFormatter(self.__formatter__)
		_handler.setLevel(severity)
		self.handlers[handler] = _handler
		self.logger.addHandler(_handler)
		return True
	#
	
	def getRootLevel(self, severity):
		return self.severity
	#
	
	def setRootLevel(self, severity):
		self.logger.setLevel(severity)
	#
	
	def getHandlerLevel(self, handler, severity):
		if not handler in self.handlers.keys():
			self.logError('指定のハンドラー名は登録されていません')
			return None
		#
		
		return self.handlers[handler].getLevel()
	#
	
	def setHandlerLevel(self, handler, severity):
		if not handler in self.handlers.keys():
			self.logError('指定のハンドラー名は登録されていません')
			return False
		#
		
		self.handlers[handler].setLevel(severity)
		return True
	#
	
	def setRootLevelByString(self, s):
		if type(s) is str:
			if s.upper() == 'CRITICAL':
				self.setRootLevel(jplogger.critical)
			elif s.upper() == 'ERROR':
				self.setRootLevel(jplogger.error)
			elif s.upper() == 'WARNING':
				self.setRootLevel(jplogger.warning)
			elif s.upper() == 'NOTICE':
				self.setRootLevel(jplogger.notice)
			elif s.upper() == 'INFO':
				self.setRootLevel(jplogger.info)
			elif s.upper() == 'DEBUG':
				self.setRootLevel(jplogger.debug)
			else:
				self.logWarning('不正なログレベルです。無視します')
		else:
			self.logWarning('不正な型のログレベルです。無視します')
	#
	
	def setHandlerLevelByString(self, handler, s):
		if type(s) is str:
			if s.upper() == 'CRITICAL':
				self.setHandlerLevel(handler, jplogger.critical)
			elif s.upper() == 'ERROR':
				self.setHandlerLevel(handler, jplogger.error)
			elif s.upper() == 'WARNING':
				self.setHandlerLevel(handler, jplogger.warning)
			elif s.upper() == 'NOTICE':
				self.setHandlerLevel(handler, jplogger.notice)
			elif s.upper() == 'INFO':
				self.setHandlerLevel(handler, jplogger.info)
			elif s.upper() == 'DEBUG':
				self.setHandlerLevel(handler, jplogger.debug)
			else:
				self.logWarning('不正なログレベルです。無視します')
		else:
			self.logWarning('不正な型のログレベルです。無視します')
	#
	def logCritical(self, msg):
			self.logger.critical(msg)
	
	def logError(self, msg):
			self.logger.error(msg)
	
	def logWarning(self, msg):
			self.logger.warning(msg)
	
	def logNotice(self, msg):
			self.logger.log(jplogger.notice, msg)
	
	def logInfo(self, msg):
			self.logger.info(msg)
	
	def logDebug(self, msg):
			self.logger.debug(msg)
	
	def log(self, severity, msg):
		if (severity == jplogger.critical):
			self.logger.critical(msg)
		elif (severity == jplogger.error):
			self.logger.error(msg)
		elif (severity == jplogger.warning):
			self.logger.warning(msg)
		elif (severity == jplogger.notice):
			self.logger.log(jplogger.notice, msg)
		elif (severity == jplogger.info):
			self.logger.info(msg)
		elif (severity == jplogger.debug):
			self.logger.debug(msg)
		else:
			self.logger.critical('未実装の呼び出しが行われました 重大度=' + str(severity))
			self.logger.critical(msg)
			raise NotImplementedError
	


