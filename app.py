from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
	return 'Meu primeiro app on whatsapp and python'

@app.route("/sms", methods=['POST'])
def sms_reply():
	# Respond to incoming calls  with a simple text
	# get the mensage
	msg = request.form.get('Body')

	# respond message
	resp = MessagingResponse()
	resp.message('Voce falou: {}'.format(msg))

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
