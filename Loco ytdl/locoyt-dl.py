import youtube_dl


class locyt:
    def __init__(self):
        self.ydl = youtube_dl.YoutubeDL(self.getOptions())

    def hook(self, d):
        if d["status"] == "finished":
            print("Done downloading, converting now....")

    def getOptions(self):
        return {
            "outtmpl": "D:\\YTDL\\%(title)s.%(ext)s",
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "progress_hooks": [self.hook],
        }

    def startDownload(self, url):
        self.ydl.download([url])


downloader = locyt()

url = input("Enter your url here: ")
downloader.startDownload(url)
