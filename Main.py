import os
from winreg import *


def DownloadsPath():

    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        return QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]


directory = os.fsencode(DownloadsPath())

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(DownloadsPath() + '\\' + filename)

