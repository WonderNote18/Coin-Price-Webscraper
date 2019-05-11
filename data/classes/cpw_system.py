import os
import sys

sys.path.insert(0, "../scripts")
import cpw_init
from app_handler import appLog

class SystemInfo():
	def __init__(self):
		self.system_info = {}
		self.app_info = {
		"url": None,
		"time_mode": None,
		"minutes": None,
		"start_range": None,
		"end_range": None}
		self.file_info = {}
	
	def main_init(self, args=[]):
		