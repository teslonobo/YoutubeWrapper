import os 
import yt_dlp 

class YouTubeData:
    def __init__(self):
        data_dir = os.path.join(os.path.dirname(__file__),'_Data')
        ops = ['Audio','Video']
        ops_dir = [os.path.join(data_dir,o) for o in ops]
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
            for o in ops_dir:
                if not os.path.exists(o):
                    os.mkdir(o)
        self.d_drive = data_dir
        self.options = ops
        self.ops_drive = ops_dir

class YouTube_DL(YouTubeData):
    def __init__(self,url:str,option:str,link_type:bool):
        super().__init__()
        self.option = option
        self.url = url
        self.link_type = link_type

    def createFormatting(self) -> dict:
        format = self.option
        if format == 'Audio':
            ydl_opts = {
                "format": "bestaudio[ext=m4a]",
                "outtmpl": os.path.join(self.ops_drive[0], "%(title)s.%(ext)s"),
                "yes-playlist": self.link_type,
                'quiet': True,
            }
            return ydl_opts
        elif format == 'Video':
            ydl_opts = {
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
                "outtmpl": os.path.join(self.ops_drive[1], "%(title)s.%(ext)s"),
                "yes-playlist": self.link_type,
                'quiet': True,
            }
            return ydl_opts
        
    def download_YTLink(self):

        ydl_opts = self.createFormatting()
        url = self.url

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
            except FileExistsError as FeE:
                pass
            except KeyboardInterrupt:
                exit(0)