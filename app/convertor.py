import config
import os
import xml.etree.ElementTree as xml


def convert_csv_to_xml(csv_doc):
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

    base_name = os.path.basename(csv_doc.name)
    file_name = f'{config.xml_path}/{os.path.splitext(base_name)[0]}.xml'
    result = f'<?xml version="1.0" encoding="{config.xml_encoding}"?>{str(xml.tostring(root).decode(config.xml_encoding))}'

    with open(file_name, "w") as fh:
        fh.write(result)













