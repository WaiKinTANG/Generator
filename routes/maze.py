import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/maze', methods=['POST'])
def mazerun():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    input_value = data.get("input")
    result = {"playerAction":0}

    if input_value["nearBy"][2][1] == 2:
        result["playerAction"] = 'down'

    elif input_value["nearBy"][0][1] == 2:
        result["playerAction"] = 'up'

    elif input_value["nearBy"][1][0] == 2:
        result["playerAction"] = 'left'
    
    elif input_value["nearBy"][1][2] == 2:
        result["playerAction"] = 'right'

    elif (input_value["nearBy"][2][1] == 0) and (input_value["nearby"][1][2] == 1):
        result["playerAction"] = 'right'

    elif (input_value["nearBy"][1][0] == 0) and (input_value["nearby"][2][1] == 1):
        result["playerAction"] = 'down'

    elif (input_value["nearBy"][0][1] == 0) and (input_value["nearby"][1][0] == 1):
        result["playerAction"] = 'left'

    elif (input_value["nearBy"][1][2] == 0) and (input_value["nearby"][0][1] == 1):
        result["playerAction"] = 'up'
    
    

    logging.info("My result :{}".format(result))
    return json.dumps(input_value)