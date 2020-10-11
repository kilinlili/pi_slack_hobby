import sys
sys.path.append("plugins")
import bme280_sample
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import requests
import slackbot_settings


@respond_to("bme")
def bme280_init(message):
    bme280_sample.setup()
    bme280_sample.get_calib_param()
    message.reply("bme280 is OK")



@respond_to("tmp")
@respond_to("press")
def bme280_run(message):

    #with 構文が使えたらキレイ
    sys.stdout = open("out.txt", "w")
    bme280_sample.readData()
    sys.stdout = sys.__stdout__

    #config
    token = slackbot_settings.API_TOKEN
    channel = slackbot_settings.CHANNEL
    file = "out.txt" 
    files = {"file": open(file, "rt")}
    filename = "temp&press&hum.txt"
    param = {
        "token": token,
        "channels": channel,
        "filename": filename,
        "initial_comment": "upload",
        "title" : "slack upload.txt"
    }
    requests.post(url="https://slack.com/api/files.upload", params=param, files=files);
   

