from DontEdit import *
import random

colors = [GREEN,RED]

while True:
  try:
    random_color = random.choice(colors)
    print(f"{random_color}test{RESET}")
  except KeyboardInterrupt:
    print("KeyboardInterrupt")