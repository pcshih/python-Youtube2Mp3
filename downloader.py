import youtube_dl
import getpass

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl':'C:\\Users\\' + getpass.getuser() + '\\Downloads\\' + '%(title)s.%(ext)s',
}


def convert(url_entry):

    url = url_entry.get()

    print(url)
    url_refined = url[0:43]

    url_refined_list = [url_refined]

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url_refined_list)
    
    end = len(url)
    url_entry.delete(0,end)

    
    



if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = ["https://www.youtube.com/watch?v=HK7SPnGSxLM"]
        ydl.download(url)