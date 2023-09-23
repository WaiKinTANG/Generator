from typing import Dict, List

import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)
# Assumption:
# 1. The depth of the object as a dictionary is at most 2; that is, the value of each key can only be empty, a list of strings, or a dictionary with a depth of 1.


def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:
  # Fill in your solution here and return the correct output based on the given input
    
    class_dict = {}
    keylist = []
    for cls in classes:
        key = list(cls.keys())[0]   
        keylist.append(key)
        class_dict[key] = cls[key]
    
    result = {}
    for statement in statements:
        prefix, *suffix = statement.split('.',1)
        probable_words = []
        for key, value in class_dict.items():
            if prefix.startswith(key):
                if suffix:
                    if isinstance(value, dict):
                        for sub_key in value.keys():
                            if sub_key in keylist:
                                probable_words.append('')
                            elif sub_key.startswith(suffix[0]):
                                probable_words.append(sub_key)
                            
                    elif isinstance(value, list):
                        for item in value:
                            if item in keylist:
                              probable_words.append('')
                            elif item.startswith(suffix[0]):
                                probable_words.append(item)
                else:
                    if isinstance(value, dict):
                        probable_words.extend(value.keys())
                    elif isinstance(value, list):
                        probable_words.extend(value)
  
        probable_words = sorted(probable_words,key = str.lower)[:5]
        # sort by Alphabetical order regardless of case
        if not probable_words:
            probable_words.append('')
        result[statement] = probable_words

    return result

@app.route('/lazy-developer', methods=['POST'])
def laziness():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    c = data.get("classes")
    s = data.get("statements")
    logging.info("classsssssss: {}".format(c))
    logging.info("type of this class:  {}".format(type(c)))
    logging.info("statement {}".format(s))
    logging.info("type of this statement:  {}".format(type(s)))
    result = getNextProbableWords(c, s)
    logging.info("My result :{}".format(result))
    return json.dumps(result)