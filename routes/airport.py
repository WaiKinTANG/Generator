from typing import Dict, List

import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)
# Assumption:
# 1. The depth of the object as a dictionary is at most 2; that is, the value of each key can only be empty, a list of strings, or a dictionary with a depth of 1.


# Simple passenger class
class Passenger:

  def __init__(self, departureTime,passengers):
    for i in range(len(passengers)):
      if passengers[i].departureTime == departureTime:
        passengers[i].numberOfRequests += 1
        del self
        break
    else:
        self.departureTime = departureTime
        self.numberOfRequests = 0


  def askTimeToDeparture(self):
    self.numberOfRequests += 1
    return self.departureTime


  def getNumberOfRequests(self):
    return self.numberOfRequests
  
def execute(prioritisation_function, passenger_data, cut_off_time):
  totalNumberOfRequests = 0
  passengers = []

  # Initialise list of passenger instances
  for i in range(len(passenger_data)):
    ls = passengers.copy()
    passengers.append(Passenger(passenger_data[i],ls))

  # Apply solution and re-shuffle with departure cut-off time
  prioritised_and_filtered_passengers = prioritisation_function(passengers, cut_off_time)

  # Sum totalNumberOfRequests across all passengers
  for i in range(len(passengers)):
    totalNumberOfRequests += passengers[i].getNumberOfRequests()
  print("totalNumberOfRequests: " + str(totalNumberOfRequests))

  # Print sequence of sorted departure times
  print("Sequence of prioritised departure times:")
  prioritised_filtered_list = []
  for i in range(len(prioritised_and_filtered_passengers)):
    print(prioritised_and_filtered_passengers[i].departureTime, end=" ")
    prioritised_filtered_list.append(prioritised_and_filtered_passengers[i].departureTime)

  print("\n")
  return {
      "total_number_of_requests": totalNumberOfRequests,
      "prioritised_filtered_list": prioritised_filtered_list
  }

def prioritisation_function(passengers, cut_off_time):
    # your solution here
    # return sorted array of passenger instances
    passengers.sort(key = lambda x: x.departureTime)
    while passengers[0].departureTime < cut_off_time:
      passengers.pop(0)
    return passengers

@app.route('/airport', methods=['POST'])
def fly():
    data = request.get_json()
    logging.info("Received :{}".format(data))
    result = []
    for sample in data:
      
      dp = sample.get("departureTimes")
      cutoff = sample.get("cutOffTime")
      logging.info("dp time :{}".format(dp))
      logging.info("cutoff :{}".format(cutoff))
      result.append(execute(prioritisation_function, dp, cutoff))
    
    logging.info("My result :{}".format(result))
    return json.dumps(result)