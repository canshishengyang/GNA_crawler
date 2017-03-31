# -*- coding: UTF-8 -*-
import urllib2

import codecs # languange encode and decode
from lxml import etree #the python built in xpath module  
import urlparse
import zipfile
import os
import svn #the two packages for svn
import svn.remote
def dfs_get_zip_file(input_path,result):
    
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path+'/'+file):
            dfs_get_zip_file(input_path+'/'+file,result)
        else:
            result.append(input_path+'/'+file)
   
def zip_path(input_path,output_path,output_name):
    #本方法目前有一个缺陷，就是不能包含子目录
    
    f = zipfile.ZipFile(output_path+'/'+output_name,'w',zipfile.ZIP_DEFLATED)
    filelists = []
    dfs_get_zip_file(input_path,filelists)
    for file in filelists:
        f.write(file)
    f.close()
    return output_path+r"/"+output_name
def svn_pageurl(pj_name):
       # url = ""
        scheme ='http'
        netloc='gna.org'
        path='/svn/'
        params=''
        query='group='+pj_name
        url = urlparse.urlunparse((scheme,netloc,path,params,query,''))
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        data = res.read()
        tree = etree.HTML(data)
        content = tree.xpath("//body/div[@class='realbody']/div[@class='main']/pre/text()")[1] #这里不用extract方法！！！
        svn_url = str(content).split(' ')[2]
        svn_dir = str(content).split(' ')[3]
        return (svn_url,svn_dir)

def svn_fetch(svn_url,path):
    r = svn.remote.RemoteClient(svn_url)
    
    r.checkout(path)
        
def dfs_get_file_url(file_url,fileitem):
        
    req = urllib2.Request(file_url)
    resultlist = []
    url =""
    try:
        response = urllib2.urlopen(req)
        data = response.read()
        url = response.geturl()

        tree = etree.HTML(data)
        result_list = tree.xpath("//body/pre/a/text()")
    except Exception,e:
            print e
    for result in result_list:
        if not str(result).endswith(r"/"):
           if r"." in str(result):
             fileitem['file_urls'].append(url+result)
            # print url+result
        else:
           dfs_get_file_url(url+result,fileitem)