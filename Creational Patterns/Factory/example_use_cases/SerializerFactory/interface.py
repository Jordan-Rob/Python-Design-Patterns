from abc import ABCMeta, abstractmethod

class ISerializer(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def serialize():
        "interface class method"

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist