# main file - created by acer51-doctom on 23/03/2026 (DD-MM-YYYY)

import os
import time

def prompt_for_path: # function to prompt for the path
    path_provided = input("Please input the path to the root of your SD Card (eg: E:\)"
    
    if not os.path.exists(path_provided):
        raise SystemExit(f"Error! The External device provided has not been found. Maybe a typo?")
    else:
        print("Thanks!")