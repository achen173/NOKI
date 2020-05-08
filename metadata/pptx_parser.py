# import zipfile
# import xml.etree.ElementTree as ET
# import re
# import os
# from os import listdir
# import collections
# import json as js
# from common_lib import *

# revision = {    # key = id, 
# "Revision": "RevisionNumber",
# "Created": "CreatedDate",
# "Modified": "ModifyDate",
# "Totaltime": "TotalEditTime",
# }

# dc_id = [ "Title","Subject","Creator","Description"]

# def main(filename, tagname, sort, json, tab):
#     zf = zipfile.ZipFile(filename)
#     data = {}
#     temp = []
#     PreviewImage = ""
#     tempstr = ""
#     for name in zf.namelist():
#         if 'docProps/' in name:
#             if('jpeg' in name):
#                 PreviewImage = "(Binary data " + str(zf.getinfo(name).file_size) + " bytes, use -b option to extract)"
#             else:
#                 root = ET.fromstring(zf.read(name))
#                 for child in root:
#                     if(len(child) == 0):
#                         temp.append((child.tag, re.sub(r'\{[^()]*\}', '', child.tag), str(child.text), "/dc/" in child.tag))
#                     else:   # may need to fix this later
#                         mylayer = child[0]
#                         if(len(mylayer[0]) == 0):
#                             tempstr = str(child[0][0].text)
#                             for i in range(1, len(child[0])):
#                                 tempstr += ", " + str(child[0][i].text)
#                         elif(len(mylayer[0][0]) == 0):
#                             tempstr = str(child[0][0][0].text)
#                             for i in range(1, len(child[0])):
#                                 tempstr += ", " + str(child[0][i][0].text)
#                         temp.append((child.tag, re.sub(r'\{[^()]*\}', '', child.tag), tempstr, "/dc/" in child.tag))

#     data = default_s(temp)
#     data = collections.OrderedDict(data.items())
#     data.update({'PreviewImage': [PreviewImage, False]})
#     data.move_to_end('PreviewImage', last=False)

#     if sort:
#         if not tagname and (not json or not tab):
#             data = formatTags(data)
#         data = sorting(data)
#     else:
#         if not tagname and not json and not tab:
#             data = formatTags(data)
            
#     if tab:
#         if not tagname and not json and not sort:
#             data = formatTags(data)
#             return TabformatPrintData(formatReturnData(data))
#         elif tagname and not json:
#             return TabformatPrintData(formatReturnData(data))
#         elif json:
#             for tag in data:
#                 if tag in dc_id: # and tag != "LastModifiedBy" and tag != "RevisionNumber":
#                     word = "XMP::dc"
#                 elif tag is "PreviewImage":
#                     word = "Extra"
#                 else:
#                     word = "OOXML::Main"
#                 data[tag] = {"id":data[tag][1],"table":word,"val":data[tag][0]}
#             return formatPrintDataJSON(data)

#     if json:
#         data = collections.OrderedDict(data.items())
#         data.update({'SourceFile':[filename,False]})
#         data.move_to_end('SourceFile', last=False)
#         return formatPrintDataJSON(formatReturnData(data))

#     return formatPrintData(formatReturnData(data))

# def default_s(temp):
#     data = {}
#     for entry in temp:
#         text = entry[2]
#         tag = entry[1][0].capitalize()+entry[1][1:]
#         if entry[2] == "false":
#             text = "No"
#         if tag in revision:
#             tag = revision[tag]
#         if "T" in text and ":" in text:
#             text = text.replace("T"," ")
#         data[tag] = [text, entry[1]]
#     return data
