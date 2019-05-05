import sys
sys.path.insert(0, '../scripts')

import app_handler

time_vars = ['-s', '-r']
arg_vars = sys.argv

if __name__ == "__main__":
	if len(arg_vars) >= 2:
		if time_vars[0] in arg_vars:
			pass
		elif time_vars[1] in arg_vars:
			pass
	else:
		exit("Useage: main.py url [-s minutes | -r start end]")
		