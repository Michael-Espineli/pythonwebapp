import signal
import sys
from types import FrameType
from flask import Flask, request, jsonify
from utils.logging import logger
import os

@app.route('/login')
def login():

        return "Hello Login.py file"
