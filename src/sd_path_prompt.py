# Prompts user for SD Card path

import os
import time

while True:
    sd_card_path = input("What is the path of your SD Card? ") # space is intended
    
    if os.path.exists(sd_card_path):
        print("SD Card volume exists.") # temporary
    
    else:
        print("Volume does not exist. Maybe wrong input?\n")
        print("Let's try again in 5 seconds.\n")
        time.sleep(5)