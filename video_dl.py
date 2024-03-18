from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

def download_video(link: str, SAVE_PATH: str):
    try:
        # Attempt to access the YouTube video
        yt = YouTube(link)
    except (RegexMatchError, VideoUnavailable):
        print("Invalid YouTube URL or Video Unavailable!")
        return 0

    streams = yt.streams.filter(file_extension='mp4')

    if streams:

        # Get the highest resolution stream
        highest_resolution_stream = streams.get_highest_resolution()

        try:
            # Download the video
            highest_resolution_stream.download(output_path=SAVE_PATH)
            print('Task Completed!')
            return 1
        except:
            print("Some Error!")
            return 0
            
    else:
        print("No MP4 streams available for download.")
