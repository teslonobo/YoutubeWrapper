from YouTubeDL_Wrapper import YouTube_DL


url = 'https://www.youtube.com/watch?v=viAk4pUCzSs'
url = 'https://www.youtube.com/watch?v=T6eK-2OQtew&list=RDCLAK5uy_k1VVBVsS6pu1pVkYZK2B0EWic3i4j_TY4&index=2'
option = 'Audio'

youtube_link = YouTube_DL(url,option).download_playlist()
