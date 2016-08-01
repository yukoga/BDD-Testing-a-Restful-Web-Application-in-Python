# -*- coding: UTF-8 -*-
from app.application import app
from flask import request, jsonify

USERS = {}

GET = 'GET'

@app.route("/user/<username>", methods=[GET])
def access_uesrs(username):
    if request.method == GET:
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)

