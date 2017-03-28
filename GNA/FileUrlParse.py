import re
import urllib2

import codecs # languange encode and decode
from lxml import etree #the python built in xpath module  


import pprint
import svn #the two packages for svn
def svn_pageurl(pj_name):
       # url = ""
        scheme ='http'
        netloc='gna.org'
        path='/svn/'
        params=''
        query='group='+pjname
        url = urlparse.urlunparse((scheme,netloc,path,params,query))
        return url

def svn_fetch(svn_url):
    pass    
def dfs_get_file(file_url,fileitem):
        
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
              fileitem['sad'].append(url+result)
        else:
           dfs_get_file(url+result,fileitem)