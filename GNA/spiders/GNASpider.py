import scrapy
import urlparse
import logging
import scrapy.spider

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
        #重写了scrapy的气势函数
        scheme ='http'
        netloc='gna.org'
        path='/search'
        params=''
        i = 0
        query='type_of_search=soft&words=%2A&type=1&offset='+str(i)+'&max_rows=25'
       
        start_url = urlparse.urlunparse((scheme,netloc,path,params,query,'results'))
       
        yield scrapy.Request(start_url,callback=self.parse_projectlist,dont_filter=False)
        
    def parse_project_files(self,response):
        #获取所有的文件的下载地址
        fileitem = FileItem()
        file_urls = []
        fileitem['file_urls'] = file_urls
        dfs_get_file_url(response.url,fileitem) 
        #获取svn的地址
       # svn_pageurl
        yield fileitem    

    def parse_projectlist(self, response):
        items = response.xpath("//body/div[@class='realbody']/div[@class='main']/table[@class='box']/tr/td/a/@href").extract()
    
        for i in items:
            pj_item = PjItem()
            pj_name = str(i).split('..')[-1]
            url = "http://gna.org/"+pj_name
            #记录项目的名字
            pj_item['pj_name'] = pj_name
          
            yield scrapy.Request(url,callback = self.parseProjectMain,meta={'pj_item':pj_item},dont_filter=False)
            
    def parse_member_list(self,response):
        member_item = MemberItem()
        member_list = response.xpath("//body/div[@class='realbody']/div[@class='main']/table[@class='box']/tr/td[2]/a/text()").extract()  
        member_item['member_list'] = member_list
        member_item['pj_name'] = pj_item['pj_name']
        yield member_item

    def parseProjectMain(self,response):
        pj_item = response.meta['pj_item']
        #记录项目的描述信息等内容。
        desc = ''
        decriptions = response.xpath("//body/div[@class='realbody']/div[@class='main']/div[@class='indexcenter']/p/text()").extract()
        for de in decriptions:
            desc += str(de)
        pj_item['pj_desc'] = desc
        
        #项目的状态，statble or release 等状态
        status =str(decriptions[-1]).split('/')[-1]
        pj_item['pj_status'] = status

        #项目遵循的开源协议
        license = response.xpath("//body/div[@class='realbody']/div[@class='main']/div[@class='indexcenter']/p/a/text()").extract()[-1]
        pj_item['pj_license'] = license

        #项目的日期
        
        
        yield pj_item
        member_url = 'http://gna.org/project/memberlist.php?group=' + pj_item['pj_name']
        yield scrapy.Request(member_url,callback = self.parse_member_list,meta={'pj_item':pj_item},dont_filter = False)
        download_url = 'http://download.gna.org/'+ pj_item['pj_name'] + '/'
        yield scrapy.Request(download_url,callback = self.parse_project_files,dont_filter = False)
        
       
       
       
        