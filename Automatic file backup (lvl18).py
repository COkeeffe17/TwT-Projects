# Automatic file backup. I had to just copy this one, as I had no idea that schedule and shutil even existed. IU did however notice that his use of the lambda function was unnecessary, although that may be because of a recent update or something.
# This obviously doesnt work without a real directory in it, but I did test it with my own paths and it worked.

import time
import os
import schedule
import datetime
import shutil

# Important info
source = "(Source directory)"
destination = "(Destination directory)"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")

    except FileExistsError:
        print(f"Folder already exists in: {dest}")

# Regular repetition
schedule.every().sunday.at("21:00").do(copy_folder_to_directory, source, destination)

# Check every minute
while True:
    schedule.run_pending()
    time.sleep(60)
