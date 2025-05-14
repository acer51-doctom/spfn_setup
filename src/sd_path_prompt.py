# Prompts user for SD Card path

import os

sd_card_path = input("What is the path of your SD Card? ") # space is intended

if os.path.exists(sd_card_path):
    print("SD Card volume exists.")

else:
    print("Volume does not exist. Maybe wrong input?")