import scrapy
import urlparse
import logging
import scrapy.spider

class GNASpider(scrapy.spider.Spider):
    name = "GNASpider"
    length = 100 
    logger = logging.getLogger()
    def svnurl():
        url = ""
        return url
        
    def start_requests(self):
       
        scheme ='http'
        netloc='gna.org'
        path='/search'
        params=''
        i = 0
        query='type_of_search=soft&words=%2A&type=1&offset='+str(i)+'&max_rows=25'
        #return super(GNASPider, self).start_requests()
        start_url = urlparse.urlunparse((scheme,netloc,path,params,query,'results'))
        
        yield scrapy.Request(start_url,callback=self.parseProjectList,dont_filter=False)
        
        
    def parseProjectList(self, response):
        items = response.xpath("//body/div[@class='realbody']/div[@class='main']/table[@class='box']/tr/td/a/@href").extract()
        
        for i in items:
            url = "http://gna.org/"+str(i).split('..')[-1]
            self.logger.info(url)
         #   yield scrapy.Request()
            
    def parseProjectMain(self,response):
        
        pass
       # return super(GNASPider, self).parse(response)
