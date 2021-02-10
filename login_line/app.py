from urllib.parse import urlencode

import requests
from flask import Flask, redirect, request

app = Flask(__name__)
app.secret_key = 'super secret key'
channel_id = '1111111111111111'
secret = '222222222222222'
token = ''
redirect_uri = 'http://127.0.0.1:5000/oauth/callback'


@app.route('/')
def index():
    return 'hello'


@app.route('/login')
def oauth():
    url = "https://access.line.me/oauth2/v2.1/authorize?"
    data = {
        "response_type" : "code",
        "client_id" : channel_id,
        "redirect_uri" : redirect_uri,
        "state" : "hZiPmLtZxa",
        "scope" : "profile"
    }
    url = url + urlencode(data)

    return redirect(url)



@app.route('/token')
def token():
    url ="https://api.line.me/oauth2/v2.1/token"
    header = {
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type" : "authorization_code",
        "code" : token,
        "redirect_uri" : redirect_uri,
        "client_id" : channel_id,
        "client_secret" : secret
    }

    resp = requests.post(url=url, data=data, headers=header)
    print (resp.text)

    return redirect('/')



@app.route('/oauth/callback')
def callback():
    global token
    token = request.args.get('code')
    return redirect('/token')


if __name__ == "__main__":
    app.run()