# -*- coding: UTF-8 -*-
import scrapy
import urlparse
import logging
import scrapy.spider
import sys  


from GNA.FileUrlParse import dfs_get_file_url
from GNA.FileUrlParse import svn_pageurl

from GNA.items import PjItem 
from GNA.items import FileItem
from GNA.items import MemberItem
class GNASpider(scrapy.spider.Spider):
    name = "GNASpider"
    length = 100 
    logger = logging.getLogger()
    def start_requests(self):
        reload(sys)  
        sys.setdefaultencoding('utf8')   
        #重写了scrapy的起始函数
        scheme ='http'
        netloc='gna.org'
        path='/search/'
        params=''
        offset = 1300
        query='type_of_search=soft&words=%2A&type=1&max_rows=25&offset='+str(offset)
       #说明一下关键字段 max_row：该页面一共显示多少个项目
                        #offset：当前的偏移量，也就是从第几个项目开始。目前GNA！的服务器上共有一千四百来个项目
        start_url = urlparse.urlunparse((scheme,netloc,path,params,query,''))
      #  offset = 1300
        yield scrapy.Request(start_url,callback=self.parse_projectlist,meta={'offset':offset},dont_filter=False)
    
    def parse_project_files(self,response):
        pj_item = response.meta['pj_item']

        #获取所有的发行文件的下载地址
        
        fileitem = FileItem()
        file_urls = []
        fileitem['file_urls'] = file_urls
        fileitem['pj_name'] = pj_item['pj_name']
        dfs_get_file_url(response.url,fileitem) 
        #获取svn的地址
        tp_svn = svn_pageurl(fileitem['pj_name'])
        fileitem['tp_svn'] = tp_svn
        yield fileitem    

    def parse_projectlist(self, response):
        items = response.xpath("//body/div[@class='realbody']/div[@class='main']/table[@class='box']/tr/td/a/@href").extract()
        offset = response.meta['offset']
        for i in items:
            pj_item = PjItem()
            pj_path = str(i).split('..')[-1]
            url = "http://gna.org"+pj_path
            #记录项目的名字
            pj_item['pj_name'] = str(pj_path).split('/')[-1]
          
            yield scrapy.Request(url,callback = self.parseProjectMain,meta={'pj_item':pj_item},dont_filter=False)
    
        end_next = response.xpath("//body/div[@class='realbody']/div[@class='main']/h5[@class='nextprev']/em/text()").extract()
        next_url = 'http://gna.org/search/?type_of_search=soft&words=%2A&type=1&max_rows=25&offset='
      
        if len(end_next)==0:
            offset += 25
            yield scrapy.Request(next_url+str(offset),callback=self.parse_projectlist,meta={'offset':offset},dont_filter=False)
            
        elif len(end_next)!=0 and str(end_next[-1])==r"Next Results":
            pass
        else:
            offset += 25
            yield scrapy.Request(next_url+str(offset),callback=self.parse_projectlist,meta={'offset':offset},dont_filter=False)
            
    
    def parse_member_list(self,response):
        pj_item = response.meta['pj_item']
        member_item = MemberItem()
        
        member_list = response.xpath("//body/div[@class='realbody']/div[@class='main']/table[@class='box']/tr/td[2]/a/text()").extract() 
        member_content = ''
        for member in member_list:
            member_content+=str(member)+r";"
        
        member_item['member_content'] = member_content
        member_item['pj_name'] = pj_item['pj_name']
        yield member_item

    def parseProjectMain(self,response):
        pj_item = response.meta['pj_item']
        #记录项目的描述信息等内容。
        desc = ''
        decriptions = response.xpath("//body/div[@class='realbody']/div[@class='main']/div[@class='indexcenter']/p/text()").extract()
        for de in decriptions:
            de.encode('utf-8')
            desc += str(de)
        pj_item['pj_desc'] = desc
        
        #项目的状态，statble or release 等状态
        status =str(decriptions[-1]).split('/')[-1]
        pj_item['pj_status'] = status

        #项目遵循的开源协议
        license = response.xpath("//body/div[@class='realbody']/div[@class='main']/div[@class='indexcenter']/p/a/text()").extract()[-1]
        pj_item['pj_license'] = license

        #项目的日期
        date = response.xpath("//body/div[@class='realbody']/div[@class='main']/div[@class='indexcenter']/p/text()").extract()[-3]
        pj_item['pj_date'] = date
        
        yield pj_item
        member_url = 'http://gna.org/project/memberlist.php?group=' + pj_item['pj_name']
        yield scrapy.Request(member_url,callback = self.parse_member_list,meta={'pj_item':pj_item},dont_filter = False)
        download_url = 'http://download.gna.org/'+ pj_item['pj_name'] + '/'
        yield scrapy.Request(download_url,callback = self.parse_project_files,meta={'pj_item':pj_item},dont_filter = False)
        
       
       
       
        