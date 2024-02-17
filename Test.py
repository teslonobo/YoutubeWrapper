from YouTubeDL_Wrapper import YP

url = 'https://www.youtube.com/playlist?list=PLcGkkXtask_fghbI0Edu-ZmsfgO8dh09I'
option = 'audio'
outpath = 'Resized'
youtube_link = YP(url,option,outpath)
youtube_link.download_playlist()