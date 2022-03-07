from flask import Flask, request
import requests as re
import time

app = Flask(__name__)

def log_request(data:dict, url:str):
    unix_time = int(time.time())

    with open ("Logs.txt", "a")  as f:
        f.write(f"{unix_time} {data} {url}\n")

@app.route("/send", methods = ['POST'])
def send():
    webhook_url = request.headers['Webhook']
    content_data = request.json

    response = re.post(webhook_url, json=content_data)

    success = response.status_code == 204
    if success:
        log_request(content_data, webhook_url)
        return "Success", 200
    else:
        return response.json()['message'], response.status_code


if __name__ == "__main__":
    app.run()