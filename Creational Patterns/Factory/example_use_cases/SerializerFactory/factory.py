from serialize_json import JsonSerializer
from serialize_xml import XmlSerializer

js = JsonSerializer()
xs = XmlSerializer()

class SerializeSong:

    @staticmethod
    def get_serializer(song, format):
        if format == 'JSON':
            return js.serialize(song)
        elif format == 'XML':
            return xs.serialize(song)
        else:
            raise ValueError(format)