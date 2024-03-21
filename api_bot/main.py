import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from toml import load
from datetime import datetime
from dateutil import tz
import logging

# import da file che creiamo noi custom
from utils import SetCustomTimeInLogger
import route_api


""" A logger for entire application"""
# logging.basicConfig(filename = 'Log/api_' + datetime.now().replace(tzinfo = tz.gettz('Europe/Rome')).isoformat("_", "seconds").replace(":", "-")[:-6] + '.log', filemode = 'w', format = '%(asctime)s %(name)s %(levelname)s %(message)s', datefmt = '%Y-%m-%d %H:%M:S')
logging.Formatter.converter = SetCustomTimeInLogger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# import della cartella con le porte per l'uscita del localhost
config = load('/Users/tortelloste/Desktop/chatbot-site/api_bot/Config/config.toml')
app = FastAPI()

origins = [config["API"]["url"] + ":" + config["API"]["port"]]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

app.include_router(route_api.router)

if __name__ == '__main__':
    uvicorn.run(app, host = config["API"]["url"].replace("http://", ""), port = int(config["API"]["port"]))
    print("running")