from app.lib.constants import measured_power, environment_factor

def rssi_to_distance(anchor, rssi_value):
  return pow(10, ((measured_power - rssi_value)/(10 * environment_factor[anchor - 1])))