from sys import exit
from decouple import config
from api.config import config_dict
from api import create_app
from sys import exit

DEBUG = config('DEBUG', default=False, cast=bool)

config_mode = 'Debug' if DEBUG else 'Production'

try:
    APP_CONFIGURATION = config_dict[config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid APP Config Mode. Expected Values are [Debug, Production]')

app = create_app(APP_CONFIGURATION)

if __name__ == "__main__":
    if DEBUG:
        app.run()
    else:
        app.run(use_reloader=False)
