from DontEdit import *
import random

colors = [GREEN,RED,BLUE]

while True:
  try:
    random_color = random.choice(colors)
    print(f"{random_color}test")
  except KeyboardInterrupt:
    print("KeyboardInterrupt")