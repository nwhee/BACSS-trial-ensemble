import json
import os
import csv

filt_instagram_dir = "ensemble_data/filtered_instagram"
filt_tiktok_dir = "ensemble_data/filtered_tiktok"

date_with_count_instagram = {}
date_with_count_tiktok = {}

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
                analyze_instagram(data, filename) if platform == "instagram" else analyze_tiktok(data, filename)

    write_to_csv(platform)
    

def analyze_instagram(data, filename):
    split_filename = filename.split("_")
    date = split_filename[1]
    # time = split_filename[2].split(".")[0]
    count = data["data"]["count"]
    if date in date_with_count_instagram:
        date_with_count_instagram[date] += count
    else:
        date_with_count_instagram[date] = count
    

def analyze_tiktok(data, filename):
    split_filename = filename.split("_")
    date = split_filename[1]
    # time = split_filename[2].split(".")[0]
    for post in data["data"]:
        play_count = post["statistics"]["play_count"]
        comment_count = post["statistics"]["comment_count"] 
        if date in date_with_count_tiktok:
            date_with_count_tiktok[date]["plays"] += play_count
            date_with_count_tiktok[date]["comments"] += comment_count
        else:
            date_with_count_tiktok[date] = {"plays": play_count, "comments": comment_count}


def write_to_csv(platform):
    csv_filename = f"date_with_count_{platform}.csv"

    with open(csv_filename, mode = "w") as f:
        writer = csv.writer(f)
        if platform == "instagram":
            for key, value in sorted(date_with_count_instagram.items()):
                writer.writerow([key, value])
        else:
            for key, value in sorted(date_with_count_tiktok.items()):
                writer.writerow([key, value])

# load_json("instagram")
load_json("tiktok")