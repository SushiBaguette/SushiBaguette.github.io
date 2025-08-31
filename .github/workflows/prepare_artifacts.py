import os, shutil
import argparse

# Below copies the latest index to the top-level index.html.
# TODO: Also build the index html

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--workspace", type=str)
args = parser.parse_args()

workspace_root = args.workspace
print(workspace_root)

blog_folder_path = os.path.join(workspace_root, "blog")
top_level_index_path = os.path.join(workspace_root, "blog", "index.html")

# Behold possibly the ugliest possible way to get the latest directory
latest_month_dir = ""
for entry in os.scandir(blog_folder_path):
    if entry.is_dir():
        latest_month_dir = max(latest_month_dir, os.path.abspath(entry.path))

latest_month_index_path = os.path.join(latest_month_dir, "index.html")

print("copy source and destination:")
print(latest_month_index_path)
print(top_level_index_path)

shutil.copyfile(latest_month_index_path, top_level_index_path)

# Prepare everything to copy in a separate folder to ignore .scripts