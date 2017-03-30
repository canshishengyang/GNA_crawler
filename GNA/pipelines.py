# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.htmlf
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

from GNA.DAO import insert_into_pj
from GNA.DAO import insert_into_files
from GNA.DAO import if_project_exists
from GNA.DAO import selectMD5
from GNA.DAO import delete_project
from GNA.DAO import if

from GNA.Panic import panic

from GNA.items import FileItem
from GNA.items import PjItem
from GNA.items import MemberItem

from GNA.FileUrlParse import svn_fetch

from GNA.signCalc import calcmd5

import MySQLdb
import scrapy

class GnaPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,MemberItem):
             
             pass
        elif isinstance(item,PjItem):
            result = if_project_exists('',item['pj_name'])
           
            md5 = calcmd5(item['pj_name'],item['pj_desc'],item['pj_status'],item['pj'])
            #如果该pj_name不存在,就直接进行插入
            if not result:
                insert_into_pj('',item['pj_name'],item['pj_desc'],item['pj_status'],item['pj_date'],item['pj_license'])
                
            else:
            #如果pj_name存在，则进行MD5验证    
                md5now = selectMD5('Codeplex_projects',md5)
                
                if not md5now:
                    #如果md5结果不存在，进行内容更新
                    #delete_project('',item['pj_name'])
                    #insert_into_pj('',item['pj_name'],item['pj_desc'],item['pj_status'],item['pj_date'],item['pj_license'])
                    pass
                else: 
                    
                    raise DropItem("Project exists!!")    

        return item

class DownloadPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item,FileItem):
            for url in item['file_urls']:
                scrapy.Request(url)
            

        return super(DownloadPipeline, self).get_media_requests(item, info)


    def item_completed(self, results, item, info):
        db=connect_db()
        if isinstance(item,CommitItem):
            for tp in results:
               if tp[0]==True:
                    id = select_id_by_pjname(item['pj_name'])
                    if not id:
                        panic(r"the project name does't exists !!!") # en taro Linus
                    else:
                       
                        if not if_file_exists('GNA_files',id[0][0],item['commit_id']):
                            
                           
                            upload_to_commonstorage('./codes/full/'+str(tp[1]['path']).split('/')[-1])
                            insert_into_files(scheme,str(tp[1]['path']).split('/')[-1],str(id[0][0]))
                        
        else:
            pass
        return item