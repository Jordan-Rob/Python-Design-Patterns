from factory import SerializeSong
from interface import Song

song = Song('3', 'Money Trees', 'Kendrick Lamar')
print(song)
json_string = SerializeSong.get_serializer(song, 'JSON')
xml_string = SerializeSong.get_serializer(song, 'XML')
print(json_string)
print(xml_string)