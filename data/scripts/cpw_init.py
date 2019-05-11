from app_handler import sysInfo, appLog

def read_args(args=[]):
	from random import randint
	args_len = len(args)
	module_flags = []
	args_info = {
	"url": None,
	"time_mode": None,
	"minutes": None,
	"start_range": None,
	"end_range": None
	}
	
	if args_len == 1:
		module_flags.extend([1, "Missing webhook url"])
	else:
		url = args[1]
		url_is_string = isinstance(url, str)
		if not url_is_string:
			module_flags.extend([1, "Arg url not type string"])
		
		if args_len == 2:
			args_info['url'] = url
			args_info['time_mode'] = "Random"
			module_flags.extend([0, ""])
		elif args_len == 3:
			module_flags.extend([1, "Missing time values for time_mode"])
		else:
			try:
				time_mode = args[2].lower()
				tm_is_string = isinstance(url, str)
				if not tm_is_string:
					module_flags.extend([1, "Arg time_mode not type string"])
			except:
				module_flags.extend([2, "Arg time_mode is not case-sensitive"])
			
			if time_mode not in ['-r', '-f']:
				module_flags.extend([1, "Invalid time_mode value"])
			
			if time_mode == '-r':
				args_info['url'] = url
				args_info['time_mode'] = 'Range'
				
				if args_len == 4:
					module_flags.extend([1, "Missing end_range value"])
				elif args_len == 5:
					start_range = args[3]
					end_range = args[4]
					args_info['start_range'] = start_range
					args_info['end_range'] = end_range
				else:
					module_flags.extend([1, "Too many arguments provided"])
			elif time_mode == 'f':
				args_info['url'] = url
				args_info['time_mode'] = 'Range'
				
				if args_len == 4:
					minutes = args[3]
					args_info['minutes'] = minutes
				elif args_len == 5:
					module_flags.extend([1, "Too many args for Fixed time_mode"])
				else:
					module_flags.extend([1, "Incorrect syntax"])
	
	try:
		flag_pass = module_flags[0]
		flag_comment = module_flags[1]
	except IndexError:
		appLog.logger.error("Range error internal var module_flags")
		exit("error: range error internal var module_flags")
	else:
		if flag_pass == 0:
			appLog.logger.info("Args read successfully")
			sysInfo.main_init_args(args=args_info)
		elif flag_pass == 1:
			appLog.logger.error(flag_comment)
			quit("error: " + flag_comment[0].upper() + flag_comment[1:])
		elif flag_pass == 2:
			appLog.logger.warning(flag_comment)
			quit("internal error: " + flag_comment[0].upper() + flag_comment[1:])
		else:
			appLog.logger.error("Invalid flag info.")
			quit("internal error: invalid flag info")