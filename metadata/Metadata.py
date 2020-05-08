import zipfile
import xml.etree.ElementTree as ET
import re
import collections


def metadata(filename):
    zf = zipfile.ZipFile(filename)
    data = {}
    for name in zf.namelist():
        if 'docProps/app.xml' in name:
            root = ET.fromstring(zf.read(name))
            for child in root:
                if('Application' in str(re.sub(r'\{[^()]*\}', '', child.tag))):
                    if('Microsoft Office Word' in child.text):
                        data = docx(filename)
                    elif('Microsoft Office PowerPoint' in child.text):
                        data = pptx(filename)
                    elif('Microsoft Excel' in child.text):
                        data = xlsx(filename)
    data = collections.OrderedDict(sorted(data.items()))
    for key in data.keys():
        print("\t\033[1;91m{:<20}  {:<35}\033[0m".format(key,  data[key]))
    return data

def pptx(filename):
    zf = zipfile.ZipFile(filename)
    data = {}
    mystr = ""
    for name in zf.namelist():
        if 'docProps/' in name:
            if('jpeg' in name):
                data["PreviewImage"] = "(Binary data " + str(zf.getinfo(name).file_size) + " bytes, use -b option to extract)"
            else:
                root = ET.fromstring(zf.read(name))
                for child in root:
                    if(len(child) == 0):
                        data[re.sub(r'\{[^()]*\}', '', child.tag)] = str(child.text)
                    else:   # may need to fix this later
                        mylayer = child[0]
                        if(len(mylayer[0]) == 0):
                            mystr = str(child[0][0].text)
                            for i in range(1, len(child[0])):
                                mystr += ", " + str(child[0][i].text)
                        elif(len(mylayer[0][0]) == 0):
                            mystr = str(child[0][0][0].text)
                            for i in range(1, len(child[0])):
                                mystr += ", " + str(child[0][i][0].text)
                        data[re.sub(r'\{[^()]*\}', '', child.tag)] = str(child.text)
    return data

def docx(filename):
    zf = zipfile.ZipFile(filename)
    data = {'SourceFile':filename}
    for name in zf.namelist():
        if 'docProps/' in name:
            root = ET.fromstring(zf.read(name))
            for child in root:
                data[re.sub(r'\{[^()]*\}', '', child.tag)] = str(child.text)
    return data

def xlsx(filename):
    zf = zipfile.ZipFile(filename)
    data = {}
    mystr = ""
    for name in zf.namelist():
        if 'docProps/' in name:
            root = ET.fromstring(zf.read(name))
            for child in root:
                if(len(child) == 0):
                    data[re.sub(r'\{[^()]*\}', '', child.tag)] = str(child.text)
                else: 
                    mylayer = child[0]
                    if(len(mylayer[0]) == 0):
                        mystr = str(child[0][0].text)
                        for i in range(1, len(child[0])):
                            mystr += ", " + str(child[0][i].text)
                    elif(len(mylayer[0][0]) == 0):
                        mystr = str(child[0][0][0].text)
                        for i in range(1, len(child[0])):
                            mystr += ", " + str(child[0][i][0].text)
                    data[re.sub(r'\{[^()]*\}', '', child.tag)] = mystr
    return data
