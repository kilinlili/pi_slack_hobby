from slackbot.bot import respond_to
from slackbot.bot import default_reply
from slackbot.bot import listen_to

#このデコレータを付けた関数はbotに向けた投稿で
#文字列が含まれるときに反応
@respond_to("now")
def reply_func(message):
    message.reply("Year!")

#参加しているチャンネルで
#bot以外に向けた投稿で反応
@listen_to("fuga")
def listen_func(message):
    message.send("Well...")
    message.reply("I'm hungry....")

@listen_to("いいね")
@listen_to("good")
def good_func(message):
    message.react("+1")
