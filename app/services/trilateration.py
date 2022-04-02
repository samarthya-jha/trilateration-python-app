from scipy.optimize import least_squares
from app.lib.constants import anchor_1, anchor_2, anchor_3

def trilateration(distance_1, distance_2, distance_3):
  x1, y1, dist_1 = (anchor_1[0], anchor_1[1], distance_1)
  x2, y2, dist_2 = (anchor_2[0], anchor_2[1], distance_2)
  x3, y3, dist_3 = (anchor_3[0], anchor_3[1], distance_3)

  def equations(guess):
    x, y, r = guess
    return (
        ( (x - x1)**2 + (y - y1)**2 - (dist_1 - r )**2,
          (x - x2)**2 + (y - y2)**2 - (dist_2 - r )**2,
          (x - x3)**2 + (y - y3)**2 - (dist_3 - r )**2
        )
    )

  initial_guess = (43, 33, 0)

  results = least_squares(equations, initial_guess)
  results.x = abs(results.x)
  return results