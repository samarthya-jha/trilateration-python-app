from app import app
from app.util import coordinates
from flask import request, jsonify

@app.route("/get-coordinates", methods = ["POST"])
def coords():
  rssi = request.json["rssiValues"]
  anchor_1, anchor_2, anchor_3 = int(rssi["anchor_1"]), int(rssi["anchor_2"]), int(rssi["anchor_3"])
  result = coordinates(anchor_1, anchor_2, anchor_3)
  return jsonify({"x": result.x[0],"y": result.x[1] })

@app.route("/")
def index():
  return "App working fine"