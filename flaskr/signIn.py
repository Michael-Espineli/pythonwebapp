import signal
import sys
from types import FrameType
from flask import Flask, request, jsonify
from utils.logging import logger
import os
from firebase_admin import credentials, firestore, initialize_app
# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

@app.route('/signIn')
def signIn():
    return 'Sign In'
