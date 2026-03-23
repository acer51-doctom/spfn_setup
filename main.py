# the program himself - created by acer51-doctom on 23/03/2026 (DD-MM-YYYY)
# last modified on 23/03/2026

import os
import time
import requests
import shutil

def prompt_for_path(): # function to prompt for the path
    path_provided = input("Please input the path to the root of your SD Card (eg: E:\)")
    
    if not os.path.exists(path_provided):
        raise SystemExit(f"Error! The External device provided has not been found. Maybe a typo?")
    else:
        print("Thanks!")
        return path_provided

def get_spfn_files_stub(): # this is the one that will be used until the files are actually up
    # paths and stuff
    file_url = "https://files.acer51.org/peekaboo.txt" # stub
    file_name = "peekaboo.txt" # stub
    folder_name = "spfn_cache"
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cache_path = os.path.join(base_dir, folder_name)
    file_path = os.path.join(cache_path, file_name)

    print("Downloading required files for Splatfestival Network...")

    # making sure the folder exists
    if not os.path.exists(cache_path):
        os.makedirs(cache_path)
        print("Created directory for temporary files.")

    # make the download (WILL OVERWRITE FILES FOR THE LATEST VERSION)
    try:
        response = requests.get(file_url, stream=True, timeout=10)
        
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Download is COMPLETE! (File overwritten)")
        else:
            print(f"Error {response.status_code}: Please report this to the repo!")
            
    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")

    return file_path

def remove_temporary_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cache_path = os.path.join(base_dir, "spfn_cache")
    
    if os.path.exists(cache_path):
        try:
            shutil.rmtree(cache_path)
            print("Successfully removed temporary files.")
        except Exception as e:
            print(f"Note: Could not delete cache folder. Error: {e}")
    else:
        print("No temporary files found; nothing to remove.")


def get_spfn_files_REAL_DONOTTOUCH(): # ONLY USE THIS WHEN WE ARE READY FOR PRODUCTION
    # paths, variables, ect...
    # TBA: replace the urls when the files are actually up
    files_to_download = {
        "spfn_plugin.wps": "https://files.spfn.net/something.wps",
        "spfn_modules.wms": "https://files.spfn.net/something.wms"
    }
    
    folder_name = "spfn_cache"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cache_path = os.path.join(base_dir, folder_name)

    print("--- Splatfestival Network Setup ---")

    # create temporary folder
    if not os.path.exists(cache_path):
        os.makedirs(cache_path)
        print(f"Directory created: {folder_name}")

    # loop for downloading
    for file_name, url in files_to_download.items():
        destination = os.path.join(cache_path, file_name)
        print(f"Downloading {file_name}...", end=" ", flush=True)
        
        try:
            # overwrites any existing .wps or .wms files in the folder
            response = requests.get(url, stream=True, timeout=15)
            
            if response.status_code == 200:
                with open(destination, "wb") as f:
                    for chunk in response.iter_content(chunk_size=1024 * 8):
                        f.write(chunk)
                print("OK!")
            else:
                print(f"FAILED (Error {response.status_code})")
                
        except Exception as e:
            print(f"\nConnection Error: {e}")

    print("-----------------------------------")
    print("Files are ready in the cache folder.")
    return cache_path

def delete_pretendo_files(path_provided): # woah! scawwy!
    # paths
    print("To be added, I'm tired")