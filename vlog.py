'''
Uses
- PAFY
https://pypi.org/project/pafy/0.5.5/
https://stackoverflow.com/questions/33698776/how-can-i-get-the-duration-of-youtube-video-with-python
- YOUTUBE_DL (required for PAFY)
https://pypi.org/project/youtube_dl/2020.3.8/

Simple Example
import pafy
url = "https://www.youtube.com/watch?v=gnHCw87Enq4&list=PLTHOlLMWEwVy52FUngq91krMkQDQBagYw"
video = pafy.new(url)
print(video)

Plalist
https://pythonhosted.org/pafy/index.html?highlight=playlist#playlist-retrieval

'''
import papy

vlog_url = 'https://www.youtube.com/playlist?list=PLTHOlLMWEwVy52FUngq91krMkQDQBagYw'
