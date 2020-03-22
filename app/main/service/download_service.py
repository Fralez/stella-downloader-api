
import os

from audiojack_service import AudioJack

def download(data):
  # Song directory
  if not os.path.exists('../songs'):
    os.mkdir('../songs')

  # Define the corresponding song path
  songpath = '../songs/{}.mp3'.format(title)

  # If the file already exists, prevent from downloading it twice (ONLY works if the songs' titles are the same)
  if not os.path.isfile(songpath):

    # Create AudioJack instance
    audiojack = AudioJack()
    # Create dictionary with the data given (dictionary structure according to audiojack module standard)
    song_dict = {
      'url': data['ytUrl'],
      'title': data['songTitle'],
      'artist': data['artist'],
      'album': data['album'],
      'img': data['imgUrl']
    }
    try:
      # Download the song and save in the songs path
      audiojack.select(song_dict, path='../songs')
    except Exception as err:
      response_object = {
        'status': 'fail',
        'message': str(err)
      }
      return response_object, 500
  
  response_object = {
    'status': 'success',
    'message': 'Song downloaded successfully.'
  }
  return response_object, 200

# BASE URL:
# http://127.0.0.1:5000/download?ytUrl=${data}&songTitle=${data}&artist=${data}&album=${data}&imgUrl=${data}