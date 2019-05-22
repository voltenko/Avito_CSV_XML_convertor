import config
import xml.etree.ElementTree as xml


def convert_csv_to_xml(csv_doc):
    """Коннвертация CSV в XML"""
    root = xml.Element('Ads', {'formatVersion': '3', 'target': 'Avito.ru'})

    for line in csv_doc.data:
        ad = xml.SubElement(root, 'ad')

        for cell in config.cells:
            if cell == 'Length' or cell == 'Amount':
                continue

            element = xml.SubElement(ad, cell)

            if cell == 'Images':
                images = line['Images'].split(',')[0:5]

                for image in images:
                    url = f'https://bmwday.ru/d/1902636/d/{image}'
                    img_element = xml.SubElement(element, 'image')
                    img_element.set('url', url)
            else:
                element.text = str(line[cell])

    return f'<?xml version="1.0" encoding="{config.xml_encoding}"?>{str(xml.tostring(root).decode(config.xml_encoding))}'












