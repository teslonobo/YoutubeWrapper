import os 
import yt_dlp 

class YouTube_Dl():
    def __init__(self, url):
        self.url = url
class YouTube_Playlist(YouTube_Dl):
    def __init__(self,url,option,outpath):
        self.option = option
        self.outpath = outpath
        super().__init__(url)
        self.url = url
    def check_format(self,my_file_path,format):
        my_file_path = self.outpath
        if not os.path.exists(my_file_path):
            os.mkdir(my_file_path)
        format = self.option 
        if format == 'audio':
            ydl_opts = {
                "format": "bestaudio[ext=m4a]",
                "outtmpl": os.path.join(my_file_path, "%(title)s.%(ext)s"),
                "yes-playlist": True,
            }
            return ydl_opts
        elif format == 'video':
            ydl_opts = {
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
                "outtmpl": os.path.join(my_file_path, "%(title)s.%(ext)s"),
                "yes-playlist": True,
            }
            return ydl_opts
        elif format != 'video' and format != 'audio':
            message = 'Must pick video, or audio '
            return message
        
    def download_playlist(self):
        directory_path = self.outpath
        url = self.url
        format = self.option
        ''' Download a Full Playlist '''
        my_file_path = os.path.abspath(directory_path)
        ydl_opts = self.check_format(my_file_path,format)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
            except FileExistsError as FeE:
                pass
            except KeyboardInterrupt:
                exit(0)
