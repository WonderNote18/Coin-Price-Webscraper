# Coin-Price-Webscraper
Reads cryptocurrency values and information for coins, which output to a Discord webhook.

### Prerequisites

The following are the minimum requirement needed to run this app:
```
Python 3
At least 8MB of disk space
At least 2GB of RAM
Internet connectivity
Preferably a server, or some online deployment service to run constantly. Otherwise a constant-running PC can work as well
```

## Enviroment Variables

The app's **main.py** function requires the following variables in order to execute:
```
webhookUrl - The URL of the webhook needed to POST information to.

(Optional) waitTimeMode - Determines how the program handles wait times between POSTs (Defaults to Random). -s for Strict mode, -r for Range mode

(Optional) fixedWaitTimeAmount - *Strict mode only.* Determines how long the program will wait to POST information to the Webhook in minutes.

(Optional) startWaitTimeAmount - *Range mode only.* Works in conjunction with endWaitTimeAmount to determine the range of time in minutes the program will wait to POST to the Webhook in minutes.

(Optional) endWaitTimeAmount - *Range mode only.* Works in conjunction with startWaitTimeAmount to determine the range of time in minutes the program will wait to POST to the Webhook in minutes.
```

## Deployment

Through your OS' terminal, call the application's **main.py** function with applicable enviroment variables. The process will continue to run until termination.

__Examples__:

	../data/main.py web.hook.url -s 60 - Waits 60 minutes in between posts
	
	../data/main.py web.hook.url -r 30 90 - Waits anywhere between 30 and 90 minutes in between posts
	
	../data/main.py web.hook.url - Waits a random amount of time in between posts (Min: 10 mins, Max: 120 mins)

## License

This project is licensed under the **GNU GENERAL PUBLIC LICENSE v3.0** - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc