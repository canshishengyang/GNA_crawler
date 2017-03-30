#!/usr/bin/python
# -*- coding: UTF-8 -*-


from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import random
import time

RackeeperHOST="172.18.108.195"
RackeeperPORT="80"
ContainerVip = "SF_VIP"
ContainerNormal = "SF_NORMAL"
ImasDevUser = "sf:admin"
ImasDevPass = "sfadmin"


"""
    Upload a local file to CommonStorage
    Parameters:
        path, a file in current folder, type of string
    Return:
        status, True if success otherwise False
"""

def upload_to_commonstorage(path):
    try:
        url = "http://" +RackeeperHOST+ "/com-sm/upload-file/"

        random.seed()
        uploadpath = path.split('/')[-1]
        print uploadpath

        count = 3
        while count > 0:
            register_openers()
            datagen, headers = multipart_encode({"upload_file": open(path,"rb"),"storage_type":ContainerVip,"filename":uploadpath,"username":ImasDevUser,"password":ImasDevPass})
            request = urllib2.Request(url, datagen, headers)
            result = urllib2.urlopen(request).read()

            print result

            if r'success' in result:
                return True

            count = count - 1
            time.sleep(random.randint(1, 10))
        
        return False

    except Exception,e:
        print e
        return False 



"""
    Download a file from CommonStorage to local drive
    Parameters:
        uri, filename in CommonStorage, type of string
        path, path in local drive, type of string
    Return:
        status, True if success otherwise False
"""
def download_from_commonstorage(uri,path):
    try:

        url = "http://" + RackeeperHOST + "/com-sm/download-file/"

        register_openers()
        datagen, headers = multipart_encode({"storage_type":ContainerVip,"filename":uri,"username":ImasDevUser,"password":ImasDevPass})
        request = urllib2.Request(url, datagen, headers)
        soft_content = urllib2.urlopen(request).read()

        # download failed
        if(r'<xml>' in soft_content):
            print 'download file failed',soft_content
            return False
        
        f = open(path,"wb")
        f.write(soft_content)
        f.close()

        return True

    except Exception,e:
        print e
        return False


"""
    Delete a file in CommonStorage
    Parameters:
        uri, filename in CommonStorage, type of string
    Return:
        status, True if success otherwise False
"""
def del_from_commonstorage(uri):
    try:

        url = "http://" +RackeeperHOST+ "/com-sm/delete-file/"

        register_openers()
        datagen, headers = multipart_encode({"storage_type":"ra","filename":uri,"username":ImasDevUser,"password":ImasDevPass})
        request = urllib2.Request(url, datagen, headers)
        result = urllib2.urlopen(request).read()

        if r'success' in result:
            return True

        # print result
        return False
    
    except Exception as e:
        print e
        return False

if __name__=='__main__':
  #  download_from_commonstorage()
    #uri=upload_to_commonstorage('e683069cd39420c3dd446ea4916194b60a579503.zip' )
    uri =    download_from_commonstorage('e683069cd39420c3dd446ea4916194b60a579503.zip','download.txt')
    print(uri)

#download_from_cloud('a6e2db353c2eca0bbbed174ea0fd9d73','.txt')

#del_from_cloud('b9e6ac8a7811c0f8ff9cab07e7c59b42')

#print random.randint(0,5)
#result=download_from_cloud_2('683a123b916d49173b8e8528d16abbb5',"c:\\varas\\result\\dynamic.dot")
#print result
    
