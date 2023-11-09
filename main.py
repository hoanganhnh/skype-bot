# This is Simple Echo Bot

import skype_chatbot
import json
from flask import Flask, request

app = Flask(__name__)

app_id = '491969b5-e209-4570-a09d-7d509c09d57e'
# Aim8Q~fpEDboyRbAAClNftZWdzs3n_DYWGsc2dsv
app_secret = 'sv48Q~CpJBRGuHyaw8eY4U96smRi.5DYHsQamaoK'

bot = skype_chatbot.SkypeBot(app_id, app_secret)


@app.route('/api/messages', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)
            bot_id = data['recipient']['id']
            bot_name = data['recipient']['name']
            recipient = data['from']
            service = data['serviceUrl']
            sender = data['conversation']['id']
            text = data['text']
            print(data)
            
            if text == 'infj':
                bot.send_message(bot_id, bot_name, recipient, service, sender, 'Anh yeu em :v')
            elif text == 'image':
                bot.send_media(bot_id, bot_name, recipient, service, sender, "image/png", "https://upload.wikimedia.org/wikipedia/vi/thumb/a/a1/Man_Utd_FC_.svg/1200px-Man_Utd_FC_.svg.png", "attachment_name")

        except Exception as e:
            print(e)

    return 'Code: 200'



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8000, debug=False)
