import xml.etree.ElementTree as xml


class XMLElement:
    """Базовый элемент XML"""

    def __init__(self, name):
        self.element = xml.Element(name)


class XMLSubElement:
    """Базовый суб-элемент XML"""

    def __init__(self, name, parent):
        self.element = xml.SubElement(name, parent)


class ImagesElement:
    def __init__(self, names):

        for name in names:





