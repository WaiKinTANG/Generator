from flask import Flask

app = Flask(__name__)
import routes.square
import routes.maze
import routes.lazy
import routes.greedy
import routes.digital
import routes.railway
import routes.chinese
