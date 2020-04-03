import os

from .audiojack_service import AudioJack

def download(data):
  # Song directory
  media_folder = 'songs/'

  # Create AudioJack instance
  audiojack = AudioJack()
  # Create tags dictionary with the data given (dictionary structure according to audiojack module standard)
  song_tags = {}
  if data.get('url') != None: song_tags['url'] = data.get('url')
  if data.get('title') != None: song_tags['title'] = data.get('title')
  if data.get('artist') != None: song_tags['artist'] = data.get('artist')
  if data.get('album') != None: song_tags['album'] = data.get('album')
  if data.get('img') != None: song_tags['img'] = data.get('img')

  try:
    # Download the song and save in the songs path
    songpath = audiojack.select(song_tags, path=media_folder)
  except Exception as err:
    response_object = {
      'status': 'fail',
      'message': str(err)
    }
    # If err is 'Media URL must be specified', then it is a 404 error;
    # else, it is an 'Unsupported file extension' in the cover art URL, then it is a 400 error.
    status = 404 if str(err).__contains__('Media') else 400
    return response_object, status
  
  response_object = {
    'status': 'success',
    'message': 'Song downloaded successfully.',
    'songpath': songpath
  }
  return response_object, 200