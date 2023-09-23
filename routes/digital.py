import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)

def digitalcolony(gen, col): #gen as number, col as string
    num = [int(col[i]) for i in range(len(col))]
    for g in range(gen):
        w = sum(num) % 10
        newnum = [((w + 10 + num[i] - num[i + 1]) % 10) for i in range(len(num) - 1)]
        nextgen = []
        for i in range(len(newnum)):
            nextgen.append(num[i])
            nextgen.append(newnum[i])
        nextgen.append(num[-1])
        num = nextgen.copy()
    return sum(num)


@app.route('/digital-colony', methods=['POST'])
def dgtl():
    data = request.get_json()
    result = []
    for i in data:
        gen = i.get("generations")
        col = i.get("colony")
        logging.info("gen: {}".format(gen))
        logging.info("colony {}".format(col))
        result.append(digitalcolony(gen, col))
    logging.info("My result :{}".format(result))
    return json.dumps(result)