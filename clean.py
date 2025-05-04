import json
import os

filt_instagram_dir = "ensemble_data/filtered_instagram"
filt_tiktok_dir = "ensemble_data/filtered_tiktok"

def load_json(platform):
    """
    Loads JSON from files

    Args: 
        platform (str): The platform where the data comes from
    """

    directory = filt_instagram_dir if platform == "instagram" else filt_tiktok_dir

    for filename in os.listdir(directory):
        if ".json" in filename:
            with open(f"{directory}/{filename}") as f:
                data = json.load(f)



load_json("instagram")