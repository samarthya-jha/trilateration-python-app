from app.services.kalman_filter import KalmanFilter
from app.services.trilateration import trilateration
from app.services.rssi_to_distance import rssi_to_distance
from app.lib.constants import process_noise, measurement_noise

def coordinates(anchor_1_rssi, anchor_2_rssi, anchor_3_rssi):
  kalman_filter = KalmanFilter(process_noise, measurement_noise)
  anchor_1_filtered_rssi, anchor_2_filtered_rssi, anchor_3_filtered_rssi = kalman_filter.filter(anchor_1_rssi), kalman_filter.filter(anchor_2_rssi), kalman_filter.filter(anchor_3_rssi)
  anchor_1_distance, anchor_2_distance, anchor_3_distance = rssi_to_distance(1, anchor_1_filtered_rssi), rssi_to_distance(2, anchor_2_filtered_rssi), rssi_to_distance(3, anchor_3_filtered_rssi)
  results = trilateration(anchor_1_distance, anchor_2_distance, anchor_3_distance)
  return results