import shutil
import os


class FileParam(object):
    oldFilePath = ""
    newFilePath = ""
    
    def __init__(self,oldFilePath,newFilePath):
        self.oldFilePath = oldFilePath
        self.newFilePath = newFilePath


def init():   
    fileParameters.append(FileParam("drawable-hdpi/","h/"))
    fileParameters.append(FileParam("drawable-xhdpi/","xh/"))
    fileParameters.append(FileParam("drawable-xxhdpi/","xxh/"))
    fileParameters.append(FileParam("drawable-xxxhdpi/","xxxh/"))
    
    print("init file paramteters success %s" % ('!!!'))
    
    
def removeOldFiles():
    for fileParam in fileParameters:
        filePath = oldFileParent+fileParam.oldFilePath+fileName
        if os.path.exists(filePath):
            os.remove(filePath)
            print("remove --%s-- success %s" % (filePath,'!!!'))
        else:
            print("--%s-- is not exists %s" % (filePath,'!!!'))
        
    print("remove old files success %s" % ('!!!'))


def replaceNewFiles():
    for fileParam in fileParameters:
        newFilePath = newFileParent+fileParam.newFilePath+fileName
        oldFilePathParent = oldFileParent+fileParam.oldFilePath
        if os.path.exists(newFilePath):
            shutil.copy(newFilePath, oldFilePathParent)
            print("copy --%s-- to --%s-- success %s" % (newFilePath,oldFilePathParent ,'!!!'))
        else:
            print("--%s-- is not exists %s" % (newFilePath,'!!!'))
        
    print("replace new files success %s" % ('!!!'))


fileParameters = []
newFileParent = """C:/Users/7UP/Desktop/android icon_vivo/android icon/"""
oldFileParent = """D:/AS_WorkSpace/QianBao/QianBao_AppClient/res/"""
fileName = "ic_launcher.png"

init()
removeOldFiles()
replaceNewFiles()

print("replace all files success %s" % ('!!!'))