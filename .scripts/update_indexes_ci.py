import os, shutil
import argparse

# TODO Delete if we give up on github actions

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--workspace", type=str)
args = parser.parse_args()
workspace_root = args.workspace

blog_folder_path = os.path.join(workspace_root, "blog")
top_level_index_path = os.path.join(workspace_root, "blog", "index.html")

# Behold possibly the ugliest possible way to get the latest directory
latest_month_dir = ""
for entry in os.scandir(blog_folder_path):
    if entry.is_dir():
        latest_month_dir = max(latest_month_dir, os.path.abspath(entry.path))

latest_month_index_path = os.path.join(latest_month_dir, "index.html")

shutil.copyfile(latest_month_index_path, top_level_index_path)