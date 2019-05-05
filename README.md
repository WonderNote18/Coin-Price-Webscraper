# Coin-Price-Webscraper
Reads cryptocurrency values and information for coins, which output to a Discord webhook.

#Useage

`Useage: main.py url [-s minutes | -r start end]`

### Prerequisites

The following are the minimum requirement needed to run this app:

- Python 3
- At least 8MB of disk space
- At least 2GB of RAM
- Internet connectivity
- Preferably a server/online deployment service to run constantly. 
- - Otherwise a constant-running PC can work as well


## Enviroment Variables

The app's **main.py** function requires the following variables in order to execute:
```
	url - The URL of the webhook needed to POST information to.

	(Optional) time_mode - Determines how the program handles wait times 
	between POSTs (Defaults to Random). -s for Strict mode, -r for Range mode.
	Strict mode requires the 'minutes' variable, and Range mode requires both 
	the 'start' and 'end' variables. Random mode will select anywhere from 
	10 - 120 minutes between posts at random.

	(Optional) minutes - [Strict mode only.] Determines how long 
	the program will wait to POST information to the Webhook in minutes.

	(Optional) start - [Range mode only.] Works in conjunction 
	with end to determine the range of time (in minutes) the 
	program will wait to POST to the Webhook.

	(Optional) end - [Range mode only.] Works in conjunction 
	with start to determine the range of time (in minutes) the 
	program will wait to POST to the Webhook.
```

## Deployment

Through your OS' terminal, call the application's **main.py** function with applicable command line arguments. The process will continue to run until termination.

__Examples__:

	../data/main.py web.hook.url -s 60 - Waits 60 minutes in between posts
	
	../data/main.py web.hook.url -r 30 90 - Waits anywhere between 30 and 90 minutes in between posts
	
	../data/main.py web.hook.url - Waits a random amount of time in between posts (Min: 10 mins, Max: 120 mins)

## License

This project is licensed under the **GNU GENERAL PUBLIC LICENSE v3.0**