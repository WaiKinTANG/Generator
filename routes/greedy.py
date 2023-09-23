def greedymonkey(w, v, f):
    val = 0
    picked = []
    rw = w
    rv = v
    for i in range(len(f)):
        if ((f[i][0] <= rw) and (f[i][1] <= rv)):
            rw -= f[i][0]
            rv -= f[i][1]
            picked.append(i)
            val += f[i][2]
    ls = picked.copy()
    
    if ls == []:
        cont = False
    else:
        cont = True
    while cont:
        rw = w
        rv = v
        val2 = 0
        ls2 = []
        for i in range(len(ls)-1):
            j = ls[i]
            rw -= f[j][0]
            rv -= f[j][1]
            val2 += f[j][2]
            ls2 += [j]
        for i in range(ls[-1] + 1, len(f)):
            if ((f[i][0] <= rw) and (f[i][1] <= rv)):
                rw -= f[i][0]
                rv -= f[i][1]
                ls2.append(i)
                val2 += f[i][2]
        if val2 > val:
            val = val2
            picked = ls2.copy()
        ls = ls2.copy()
        if ls == []:
            cont = False
    return val




#-----------------------------------------------------------------------------
import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/greedymonkey', methods=['POST'])
def greed():
    data = request.get_json()
    w = data.get("w")
    v = data.get("v")
    f = data.get("f")
    result = greedymonkey(w, v, f)
    return json.dumps(result)
