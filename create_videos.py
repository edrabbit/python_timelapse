"""
Create timelapses using ffmpeg
This assumes that the files for each timelapse have been copied to the specified source_dir
"""
import datetime
import os
import subprocess


def create_one_day_timelapse(date=None, source_dir=None, output_file=None, overwrite=False):
    """Function to create a timelapse using a subset of .jpgs in source_dir selected by the date included
    in the filename, as specified by date.
    :param date: datetime object to use as file mask for the jpgs to include
    :param source_dir: where the source .jpgs are located
    :param output_file: where the output .mp4 file should be written
    :param overwrite: boolean Should existing mp4s be overwritten? Useful if reprocessing
    """
    # ffmpeg -pattern_type glob -i "*.jpg" -framerate 30 -crf 23 -c:v libx265 -preset medium -tag:v hvc1 timelapse_full_x265_30fps_crf23_hv1_medium.mp4
    if date:
        tl_date = date.strftime("%Y%m%d")
        print(tl_date)
        file_mask = f"{tl_date}*.jpg"
    else:
        file_mask = "*.jpg"
    input = os.path.join(source_dir,file_mask)
    framerate = 30
    crf = 23
    preset = "medium"
    if overwrite:
        overwrite_param = "-y"
    else:
        overwrite_param = "-n"
    #output_file = "timelapse_full_x265_30fps_crf23_hv1_medium.mp4"
    ff_cmd = ["ffmpeg",
              overwrite_param,
              "-pattern_type", "glob",
              "-i", f'{input}',
              "-framerate",f"{framerate}",
              "-crf",f"{crf}",
              "-c:v","libx265",
              "-preset",f"{preset}",
              "-tag:v","hvc1",
              f"{output_file}"]
    print(ff_cmd)
    subprocess.run(ff_cmd)

def create_all_timelapses(source_dir=None, output_path=None,
                          first_day=None, last_day=None, overwrite=False):
    """ Create multiple timelapses from the files in source_dir into output_path starting with first_day and
    ending (inclusive) with last_day. source_dir should not have subfolders """
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    date = first_day
    while date <= last_day:
        outfile = os.path.join(output_path,f'{date.strftime("%Y%m%d")}.mp4')
        create_one_day_timelapse(date=date, source_dir=source_dir, output_file=outfile, overwrite=overwrite)
        date += datetime.timedelta(days=1)
    return


if __name__ == '__main__':
    create_all_timelapses(source_dir="/Volumes/Timelapse/goldenhour_jpgs/",
                          output_path="/Volumes/Timelapse/goldenhour_videos/",
                          first_day=datetime.date(2022, 1, 1), last_day=datetime.date(2022, 1, 31))