from PyExifTool import exiftool
files = "hello.docx"
with exiftool.ExifTool() as et:
    metadata = et.get_metadata(files)
for d in metadata:
    print("{:20.20} {:20.20}".format(d["SourceFile"],
                                         d["EXIF:DateTimeOriginal"]))