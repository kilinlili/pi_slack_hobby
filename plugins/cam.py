import cv2
from slacker import Slacker
import requests
import slackbot_settings
from slackbot.bot import respond_to

@respond_to("now")
def cap_cam(message):
    cap = cv2.VideoCapture(0) 
    ret, frame = cap.read() 
    cv2.imwrite("img.jpg", frame)
    message.reply("Take image ok")

    #files = {"file": open(img.jpg, "rb")}
    files = "/home/pi/Documents/py/pi_cam_to_slack/img.jpg"
    #params = {
    #    'token':slackbot_settings.API_TOKEN,
    #    'channnels':"C01BEK13KE2",
    #    'filename':"filename",
    #    "inittial_comment":"hogehogefugaguga",
    #    "title":"file name fuga",
    #}
    #requests.post(url="https://slack.com/api/files.upload", params=params, files = files)
    CHANNEL = "D01CB12QQHW"#direct_message
    slacker = Slacker(slackbot_settings.API_TOKEN)
    slacker.files.upload(file_=files, channels=CHANNEL)



