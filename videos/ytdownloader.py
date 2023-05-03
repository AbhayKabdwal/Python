from pytube import YouTube, Stream
import time

# Add filename here
filename = "links.txt"

with open(filename) as linksfile:
    links = linksfile.readlines()


for link in links:
    for _ in range(10):
        # try:
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        video_title = yt.title   # title of video
        video_views = yt.views   # views in video
        video_length = yt.length # length of video in seconds
        video_size = yd.filesize # size of video in bytes

        print("\nTitle: ", video_title)
        print("Views: ", video_views)
        print("Length: ", video_length//60, "minutes", video_length%60, "seconds")
        print("Size: ", video_size/(2**20), "MB")

        time.sleep(1)
        print("Donwloading... ")

        # Add folder path here
        yd.download(".\YT")
        
        print("Download complete!")
        print("\n------------------------------------")

        links.remove(link)
        break
    
        # except Exception:
        #     print(f"\nAn error occurred while accessing the data for {link}")
        #     continue

open('links.txt', 'w').close()

with open("links.txt","a") as linksfile:
    for link in links:
        linksfile.write(link)