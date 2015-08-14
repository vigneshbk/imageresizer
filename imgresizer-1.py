__author__ = 'evigkum'

import yaml
import os

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



def listFiles(folderName):
     #for (dirpath, dirnames, filenames) in os.walk(folderName):
     alist_filter = ['jpg','bmp','png','gif']
     #for imageFile in os.listdir(folderName):
     #     if imageFile[-3:] in alist_filter:
     #          #print imageFile

     allimgs = [imageFile for imageFile in os.listdir(folderName) if imageFile[-3:] in alist_filter]
     print allimgs



loadInput()
listFiles(inputDirs[0])
