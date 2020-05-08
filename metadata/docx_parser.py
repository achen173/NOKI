import zipfile
import xml.etree.ElementTree as ET
import re
import collections

class Alan:

    def metadata(self, filename):
        # try:
        zf = zipfile.ZipFile(filename)
        for name in zf.namelist():
            if 'docProps/app.xml' in name:
                root = ET.fromstring(zf.read(name))
                for child in root:
                    if('Application' in str(re.sub(r'\{[^()]*\}', '', child.tag))):
                        if('Microsoft Office Word' in child.text):
                            self.main(filename)


    def main(self, filename):
        zf = zipfile.ZipFile(filename)
        data = {'SourceFile':filename}
        temp = []
        for name in zf.namelist():
            if 'docProps/' in name:
                root = ET.fromstring(zf.read(name))
                for child in root:
                    data[re.sub(r'\{[^()]*\}', '', child.tag)] = str(child.text)
        data = collections.OrderedDict(sorted(data.items()))
        for key in data.keys():
            print("\t\033[1;91m{:<20}  {:<35}\033[0m".format(key,  data[key]))
        return data
