import skype_chatbot
import json
from flask import Flask, request

from model import get_request

app = Flask(__name__)

app_id = '491969b5-e209-4570-a09d-7d509c09d57e'
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
            
            if text.lower() == '*mu':
                bot.send_media(bot_id, bot_name, recipient, service, sender, "image/png", "https://upload.wikimedia.org/wikipedia/vi/thumb/a/a1/Man_Utd_FC_.svg/1200px-Man_Utd_FC_.svg.png", "attachment_name")
            
            res_text = get_request(text.lower())
            bot.send_message(bot_id, bot_name, recipient, service, sender, res_text)           
        except Exception as e:
            print(e)

    return 'Code: 200'



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8000, debug=False)
