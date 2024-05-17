import json
from interface import ISerializer

class JsonSerializer(ISerializer):

    def serialize(self, song):
        song_info = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }

        return json.dumps(song_info)