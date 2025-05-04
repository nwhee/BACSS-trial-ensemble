import json
import os

instagram_dir = "BACSS-trial-ensemble/ensemble_data/raw_instagram"
tiktok_dir = "BACSS-trial-ensemble/ensemble_data/raw_tiktok"

def load_json(platform):
    """
    Loads raw JSON from files

    Args: 
        platform (str): The platform where the data comes from
    """

    directory = instagram_dir if platform == "instagram" else tiktok_dir

    for filename in os.listdir(directory):
        if ".json" in filename:
            with open(f"{directory}/{filename}") as f:
                data = json.load(f)

                # filtering out files about rate limit
                if "detail" not in data:
                    write_json_to_filter_dir(
                        data,
                        f"BACSS-trial-ensemble/ensemble_data/filtered_{platform}",
                        filename)

def write_json_to_filter_dir(data, directory, filename):
    """
    Writes given JSON to a file in the given directory with the given filename
    """

    with open(f"{directory}/{filename}", "w") as f:
        json.dump(data, f, indent = 4)
    print(f"JSON data written to {directory}/{filename}")

load_json("instagram")
load_json("tiktok")