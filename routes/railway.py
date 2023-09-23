import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)

def railwaybuilder(inp):
    oup = []
    for i in inp:
        count = 0
        ls = [int(j) for j in i.split(", ")]
        p = ls[2:]
        p.sort()
        m = [(ls[0] // j) for j in p]
        ind = [0 for j in range(ls[1])]
        while ind[0] <= m[0]:
            r = ls[0]
            for j in range(len(ind)):
                r -= ind[j] * p[j]
            if r == 0:
                count += 1
            ind[-1] += 1
            for j in range(1, len(ind)):
                if ind[-j] > m[-j]:
                    ind[-j] = 0
                    ind[-j-1] += 1
                        
        oup.append(count)
    return oup

def count_combinations(arr, k):
    def count_recursive(index, target):
        if target == 0:
            return 1
        if index < 0 or target < 0:
            return 0
        return count_recursive(index - 1, target)+ count_recursive(index, target - arr[index])

    return count_recursive(len(arr) - 1, k)

def preprocess(ls):
    result = []
    for i in ls:
        a = list(map(int, i.split(",")))
        
        result.append(count_combinations(sorted(a[2:]),a[0]))
    return result

@app.route('/railway-builder', methods=['POST'])
def rail():
    data = request.get_json()
    logging.info("Data :{}".format(data))
    logging.info("Type :{}".format(type(data)))
    result = preprocess(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result)