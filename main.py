import os
import shutil
from pathlib import Path
from typing import List

VIDEO_FOLDER = Path("/home/lucat/Workspace/subs-handler/test")
SUBS_FOLDER = VIDEO_FOLDER.joinpath("Subs")

def find_videos_in_folder() -> List[Path]:
    video_files = []

    for root, dirs, files in os.walk(VIDEO_FOLDER):
        for file in files:
            if file.endswith(".mp4"):
                video_files.append(Path(root).joinpath(file))

    return video_files


def find_sub_file(video_name: str) -> Path:
    for root, dirs, files in os.walk(SUBS_FOLDER):
        for file in files:
            sub_file_path_obj = Path(root).joinpath(Path(file))
            if str(sub_file_path_obj.parent.name) == video_name:
                return sub_file_path_obj

def copy_sub_to_video(video_path: Path, sub_path: Path) -> None:
    shutil.copy(src=sub_path, dst=video_path.parent.joinpath(video_path.name))

if __name__ == "__main__":
    # Init
    print("Reorganizing subs")
    print("Video folder is " + str(VIDEO_FOLDER))
    print("Subs folder is " + str(SUBS_FOLDER))

    videos = find_videos_in_folder()
    for video in videos:
        video_sub_file = find_sub_file(video.stem)
        print(f'For file {video.name}, found sub file {video_sub_file}')

        copy_sub_to_video(video.parent.joinpath(video.stem+'.srt'), video_sub_file)
