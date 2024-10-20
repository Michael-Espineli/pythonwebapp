import signal
import sys
from types import FrameType

from flask import Flask

from utils.logging import logger
@app.route('/signIn')
def signIn():
    return 'Sign In'
