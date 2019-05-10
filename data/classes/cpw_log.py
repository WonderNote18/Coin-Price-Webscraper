import logging
import datetime
import os


class AppLogger():
	def __init__(self):
		self.logger = logging.getLogger("AppLogger")
		self.logger.setLevel(logging.DEBUG)

		self.formatter = logging.Formatter("%(asctime)s[%(levelname)s]: %(message)s", "[%I:%M:%S %p]")

		self.consoleHandler = logging.StreamHandler()
		self.consoleHandler.setLevel(logging.DEBUG)

		self.fileDate = datetime.datetime.now().strftime("%m-%d-%Y")
		if (self.fileDate + ".log") not in os.listdir("../logs"):
			newFile = open("../logs/" + self.fileDate + ".log", 'w')
			newFile.close()
		self.fileHandler = logging.FileHandler("../logs/" + self.fileDate + ".log", 'a')
		self.fileHandler.setLevel(logging.DEBUG)
		self.fileHandler.setFormatter(self.formatter)

		self.logger.addHandler(self.fileHandler)
	
	def updateLoggingFileDaily(self, newTime):
		self.fileDate = newTime.strftime("%m-%d-%Y")

		self.fileHandler.close()
		self.logger.removeHandler(self.fileHandler)

		newFile = open("../logs/" + self.fileDate + ".log", 'w')
		newFile.close()

		self.fileHandler = logging.FileHandler("../logs/" + self.fileDate + ".log", 'a')
		self.fileHandler.setLevel(logging.DEBUG)
		self.fileHandler.setFormatter(self.formatter)

		self.logger.addHandler(self.fileHandler)