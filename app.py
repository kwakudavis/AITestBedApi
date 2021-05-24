"""@package docstring
Documentation for Restful Api responsible for serving images to be processed.

More details.
"""

import os

from flask_restful import Api
from flask import Flask
from resources.Task import Task


app = Flask(__name__)

api = Api(app)


#Api interacts with individual Tasks
api.add_resource(Task, '/Task/<string:id>')

#Api interacts with all Tasks
#api.add_resource(TaskList, '/TaskList/<string:model_number>')







if __name__== '__main__':
    app.run(port=5000, debug = True)
