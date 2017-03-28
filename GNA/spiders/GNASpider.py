import scrapy
import urlparse
import logging
import scrapy.spider


from GNA.items import PjItem 
from GNA.items import FileItem
class GNASpider(scrapy.spider.Spider):
    name = "GNASpider"
    length = 100 
    logger = logging.getLogger()
  
                #pass        

        
    def start_requests(self):
       
        scheme ='http'
        netloc='gna.org'
        path='/search'
        params=''
        i = 0
        query='type_of_search=soft&words=%2A&type=1&offset='+str(i)+'&max_rows=25'
        #return super(GNASPider, self).start_requests()
        start_url = urlparse.urlunparse((scheme,netloc,path,params,query,'results'))
       
        yield scrapy.Request(start_url,callback=self.parse_projectlist,dont_filter=False)
        
    def releaseFilesParse(self,response):
        fileitem = response.meta['fileitem']
             
    def parse_projectlist(self, response):
        items = response.xpath("//body/div[@class='realbody']/div[@class='main']/table[@class='box']/tr/td/a/@href").extract()
    
        for i in items:
            pj_item = PjItem()
            pj_name = str(i).split('..')[-1]
            url = "http://gna.org/"+pj_name
            pj_item['pj_name'] = pj_name
            #self.logger.info(url)
            yield scrapy.Request(url,callback = self.parseProjectMain,dont_filter=False)
            #scrapy.http.Response
            
    def parseProjectMain(self,response):
       
        desc = ''
        decriptions = response.xpath("//body/div[@class='realbody']/div[@class='main']/div[@class='indexcenter']/p/text()").extract()
        for de in decriptions:
            desc += str(de)
        pj_item['pj_desc'] = desc
        
        fileitem = FileItem()
        file_urls = []
        fileitem['file_urls'] = file_urls
       # yield scrapy.Request('',callback= self.releaseFilesParse,meta={'fileitem':fileitem},dont_filter=False)
       
