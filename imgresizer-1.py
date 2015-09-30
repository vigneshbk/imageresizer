__author__ = 'evigkum'

import yaml
import os
import Image

inputDirs=[]
resultDir=''
resizeDim=''


def loadInput():
     stream = open("input.yaml", "r")
     docs = yaml.load_all(stream)
     for item in docs.next().items():
          if item[0]=='inputFolder':
               inputDirs.extend(item[1])
          elif item[0]=='outputFolder':
               resultDir=item[1]
          elif item[0]=='size':
               resizeDim=item[1]
          else:
               print 'BoseDK'

def listFolders(parentFolderName):
      folderList = []
      for (dirpath, subdirs, filenames) in os.walk(parentFolderName):
          for dirO in subdirs:
               folderList.append(dirpath+'/'+dirO)
      return sorted(folderList)

def listFiles(folderName):
      alist_filter = ['jpg','bmp','png','gif','jpeg','img']
      allimgs = [(folderName, imageFile) for imageFile in os.listdir(folderName) if os.path.splitext(imageFile)[1][1:] in alist_filter]
      return allimgs


def resizeFile(imageList):
      size = 128, 128
      for infile in imageList:
          outfile = '/home/evigkum/testbed-op'+'/'+ os.path.splitext(infile[1])[0] + ".jpeg"
          if infile != outfile:
               try:
                    im = Image.open(infile[0] + '/' +infile[1])
                    im.thumbnail(size)
                    im.save(outfile, "JPEG")
               except IOError as e:
                    print "cannot create thumbnail for", (infile[0] + '/' +infile[1])+e.strerror


loadInput()

print(listFiles(listFolders(inputDirs[0])[1]))
resizeFile(listFiles(listFolders(inputDirs[0])[1]))