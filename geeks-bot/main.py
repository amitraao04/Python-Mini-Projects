# from flask import Flask, request
# from googlesearch import search
# from twilio.twiml.messaging_response import MessagingResponse

# app = Flask(__name__)

# @app.route("/", methods=["POST"])
# def bot():
#     user_msg = request.values.get('Body', '').lower()
#     response = MessagingResponse()
#     q = user_msg + "geeksforgeeks.org"
#     result = [url for url in search(q, num_results=3)]
#     msg = response.message(f"--- Results for '{user_msg}' ---")
#     for res in result:
#         msg = response.message(res)
#     return str(response)

# if __name__ == "__main__":
#     app.run()

from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])
def bot():
    user_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    q = user_msg + " espn.com"  # Changed to ESPN
    result = [url for url in search(q, num_results=3)]
    msg = response.message(f"--- Results for '{user_msg}' ---")
    for res in result:
        msg.body(res)  # Changed from msg = response.message(res) to msg.body(res)
    return str(response)

if __name__ == "__main__":
    app.run()
