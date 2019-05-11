import cpw_init
import sys

sys.path.insert(0, "../classes")
from cpw_system import SystemInfo
from cpw_log import AppLogger

appLog = AppLogger()
sysInfo = SystemInfo()

def __init__(args=[]):
	cpw_init.read_args(args)