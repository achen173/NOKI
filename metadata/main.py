from metadata.docx_parser import main
# import pptx_parser
# import xlsx_parser


import zipfile
import xml.etree.ElementTree as ET
import re


def main(filename):
    try:
        zf = zipfile.ZipFile(filename)
        for name in zf.namelist():
            if 'docProps/app.xml' in name:
                root = ET.fromstring(zf.read(name))
                for child in root:
                    if('Application' in str(re.sub(r'\{[^()]*\}', '', child.tag))):
                        if('Microsoft Office Word' in child.text):
                            main(filename)
    except:
        print("Error with input file")

