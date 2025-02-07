#暫時無用
import random, os
def f_waffle_secret():
    path = r"C:\Users\1\Desktop\鬆餅秘方"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    return random_filename 
  
