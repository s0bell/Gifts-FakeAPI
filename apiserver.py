#!/usr/bin/env python
from flask import Flask, request, redirect, Response
import json, datetime, os, sys
from pymongo import Connection

connection = Connection( 'localhost', 27017 )
db = connection.giftfinder
app = Flask(__name__)


@app.route('/api/v1/interests')
def interest():
    parent_num = "parent_{0}".format(request.args.get('parent'))
    result = db[parent_num].find({},{"_id": 0})
    return Response( response = json.dumps(list(result)),
                        status = 200, mimetype = "application/json" )


#####################################
#  Exceptions and generic messages  #
#####################################

def empty_json():    
    content = {}
    return Response( response = json.dumps(content),
                        status = 200, mimetype = "application/json" )


if __name__ == "__main__":
    app.debug = True
    app.run(host = 'localhost')