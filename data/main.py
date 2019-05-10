import sys
sys.path.insert(0, '../scripts')

import app_handler

arg_vars = sys.argv

if __name__ == "__main__":
	app_handler.__init__(arg_vars)