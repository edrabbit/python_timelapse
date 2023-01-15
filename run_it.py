import datetime
import os
import create_videos
import get_files

# IMG_DIR = "/Volumes/Timelapse/goldenhour_jpgs/202201"
# VID_DIR = "/Volumes/Timelapse/goldenhour_videos/"
#
# os.makedirs(IMG_DIR, exist_ok=True)
# os.makedirs(VID_DIR, exist_ok=True)

# get_files.copy_all_files(
#     dest_dir=IMG_DIR, event="goldenhour",
#     gh_start_offset=0, gh_end_offset=15,
#     first_day=datetime.date(2022, 1, 1), last_day=datetime.date(2022, 1, 31)
# )
#
# create_videos.create_all_timelapses(
#     source_dir=IMG_DIR,
#     output_path=VID_DIR,
#     first_day=datetime.date(2022, 1, 1), last_day=datetime.date(2022, 1, 31)
# )
###

# get_files.copy_files_timespan(
#     source_dir="/Volumes/Timelapse/ftp", dest_dir="/Volumes/Timelapse/storm_test",
#     first_day=datetime.date(2023,1,4), last_day=datetime.date(2023,1,4),
#     start_time=datetime.time(16, 0, 0), end_time=datetime.time(23, 0, 0))
# create_videos.create_all_timelapses(
#     source_dir="/Volumes/Timelapse/storm_test",
#     output_path="/Volumes/Timelapse/",
#     first_day=datetime.date(2023, 1, 4), last_day=datetime.date(2023, 1, 4)
# )


#STILL NEED TO FINISH THIS
create_videos.create_full_year(
    source_dir="/Volumes/Timelapse/ftp",
    output_path="/Volumes/Timelapse/2022-EntireYear",
    year=2022, start_month=12, start_day=1
)

