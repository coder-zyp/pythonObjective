#!/usr/bin/python
import re


line = "[sdfasdfasdf]红海行动.HD.高清视频.mp4"


#
# if searchObj:
#     print("searchObj.group() : ", searchObj.group())
#
#     print("searchObj.group(1) : ", searchObj.group(1))
#
#     print("searchObj.group(2) : ", searchObj.group(2))
#
# else:
#     print("Nothing found!!")
#
#
searchObj = re.search(r'([\[|\【].*[\]|\】])(.*?)\.(.*)\.(.*)', line)
# print(searchObj.group())

searchObj = re.match(r'([\[|\【].*[\]|\】])(.*?)\.(.*)\.(.*)', line)
print("searchObj.group() : ", searchObj.group(2) + "." + searchObj.group(4))
r'([\[|\【].*[\]|\】])(.*?)\.(.*)\.(.*)', line
line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*)o(.*).*', line)

print("searchObj.group() : ", searchObj.group(1), "ssss", searchObj.group(2))