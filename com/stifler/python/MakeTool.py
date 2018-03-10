#!/usr/bin/python
# coding=utf-8
import os
import shutil

def readChannelfile(filename):
    f = open(filename, mode='r', buffering=1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
    while True:
        line = f.readline().strip('\n')
        if len(line) == 0:
            break
        else:
            channelList.append(line);
    f.close()

def backUpManifest():
    if os.path.exists('./AndroidManifest.xml'):
        os.remove('./AndroidManifest.xml')
    manifestPath = './temp/AndroidManifest.xml'
    shutil.copyfile(manifestPath, './AndroidManifest.xml')

def modifyChannel(value):
    tempXML = ''
    f = open('./AndroidManifest.xml', mode='r', buffering=1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
    for line in f:
        if line.find('ticket_android') > 0:
            line = line.replace('ticket_android', value)
        tempXML += line
    f.close()

    output = open('./temp/AndroidManifest.xml', mode='w', buffering=1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
    output.write(tempXML)
    output.close()
    print ('-------------------- step 4 --------------------')
    
    unsignApk = r'./bin/%s_%s_unsigned.apk'% (easyName, value)
    cmdPack = r'java -jar apktool.jar b temp %s'% (unsignApk)
    print(cmdPack)
    os.system(cmdPack)
    print('-------------------- step 5 --------------------')
    
    signedjar = r'./bin/%s.apk'% (value)
    unsignedjar = r'./bin/%s_%s_unsigned.apk'% (easyName, value)
    cmd_sign = r'jarsigner -verbose -keystore %s -storepass %s -signedjar %s %s %s -sigalg MD5withRSA -digestalg SHA1'% (keystore, storepass, signedjar, unsignedjar, alianame)
    print(cmd_sign)
    os.system(cmd_sign)
    print('-------------------- step 6 --------------------')
    os.remove(unsignedjar);
    

channelList = []
apkName = 'qbaoticket.apk'
easyName = apkName.split('.apk')[0]
keystore='./keystore/qianbaoticket'
storepass='geyulong'
alianame='geyulong'

output_apk_dir="./bin"
if os.path.exists(output_apk_dir):
    shutil.rmtree(output_apk_dir)

readChannelfile('./channel')
print('-------------------- your channel values --------------------')
print('channel list: ', channelList)
cmdExtract = r'java -jar apktool.jar  d -f -s %s temp'% (apkName)
os.system(cmdExtract)
print('-------------------- step 1 --------------------')

backUpManifest()
print('-------------------- step 2 --------------------')
for channel in channelList:
    modifyChannel(channel)
print('-------------------- step 3 --------------------')

if os.path.exists('./temp'):
    shutil.rmtree('./temp')
if os.path.exists('./AndroidManifest.xml'):
    os.remove('./AndroidManifest.xml')
print('-------------------- Done --------------------')

