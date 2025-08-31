import os, shutil

blog_folder_path = "./blog"
top_level_index_path = os.path.abspath("./blog/index.html")

# Behold possibly the ugliest possible way to get the latest directory
latest_month_dir = ""
for entry in os.scandir(blog_folder_path):
    if entry.is_dir():
        latest_month_dir = max(latest_month_dir, os.path.abspath(entry.path))

latest_month_index_path = os.path.join(latest_month_dir, "index.html")

shutil.copyfile(latest_month_index_path, top_level_index_path)