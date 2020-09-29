import os, hashlib
from datetime import datetime


def getHash(filename):
    try:
        with open(filename, 'rb') as f:
            m = hashlib.sha1()
            while True:
                data = f.read(8192)
                if not data:
                    break
                    m.update(data)
    except IOError as e:
        print(f"Error reading {filename}: {e}")
    return m.hexdigest()

def createFileHashDict(filename):
    d = dict(zip(('path_file', 'dt', 'sha1'), (filename, str(datetime.now()), getHash(filename))))
    return d


def getFileInfo(pathname):
    fileList = []
    for root, dirs, files in os.walk(pathname, topdown=True):
        for name in files:
            fileList.append(createFileHashDict(os.path.join(root, name)))
            print(os.path.join(root, name))
        # for name in dirs:
            # print(os.path.join(root, name))
    return fileList

DEFAULTPATH = r'C:\Users\tulon\Documents\Nikolas_T\Работа\Проекты\ЕКЦ\Регламенты\14. Регламент функц_я ИС ЕКЦ'

if __name__ == '__main__':
    inputPath = input('Введите путь: ')
    print(getFileInfo(inputPath))
    # print(getFileInfo(DEFAULTPATH))
