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
from GNA.DAO import update_project_record
from GNA.DAO import if_member_exists
from GNA.DAO import select_id_by_pjname
from GNA.DAO import connect_db
from GNA.DAO import if_file_exists
from GNA.DAO import insert_into_members
from GNA.DAO import update_members_record


from GNA.Panic import panic


from GNA.items import FileItem
from GNA.items import PjItem
from GNA.items import MemberItem


from GNA.udload2 import upload_to_commonstorage

from GNA.FileUrlParse import zip_path
from GNA.FileUrlParse import svn_fetch

from GNA.signCalc import calcmd5

from GNA.FileUrlParse import svn_fetch

import MySQLdb
import scrapy
import datetime
import os

class Printpipeline(object):
     def process_item(self,item,spider):
        if isinstance(item,FileItem):
            print 'FileItem'
        return item
class GnaPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,MemberItem):
             #result = if_member_exists('',item[''])
            md5 = calcmd5(item['member_content'])
            result = selectMD5('GNA_memberlists',md5)
            pj_id = select_id_by_pjname('GNA_projects',item['pj_name'])
            if not result:
                insert_into_members('GNA_memberlists',item['member_content'],pj_id[0][0],md5)
            else:
                if str(md5)==result[0][0]:
                   update_members_record('GNA_memberlists',result[0][0],md5)
                else:
                   raise DropItem('members_exists!!')            
       
        elif isinstance(item,PjItem):
            result = if_project_exists('GNA_projects',item['pj_name'])
           
            md5 = calcmd5(item['pj_name'],item['pj_desc'],item['pj_status'],item['pj_date'],item['pj_license'])
            #如果该pj_name不存在,就直接进行插入
            
            if not result:
                insert_into_pj('GNA_projects',str(item['pj_name']).replace("'",""),str(item['pj_desc']).replace("'",""),item['pj_status'],item['pj_date'],item['pj_license'],str(md5))
             
            else:
            #如果pj_name存在，则进行MD5验证    
                md5now = selectMD5('GNA_projects',md5)
                
                if not md5now:
                    #如果md5结果不存在，进行内容更新
                    result = select_id_by_pjname('GNA_projects',item['pj_name'])
                    update_project_record('GNA_projects',int(result[0][0]),str(item['pj_name']).replace("'",""),str(item['pj_desc']).replace("'",""),item['pj_status'],item['pj_date'],item['pj_license'],md5)
                else: 
                    
                    raise DropItem("Project exists!!")    
        elif isinstance(item,FileItem):
            #把svn获取的结果用tuple传递回来。
            tp = item['tp_svn']
            
            svn_url = tp[0]
            svn_name = tp[1]
            svn_path = r"./code/"+svn_name
            try:
                svn_fetch(svn_url,svn_path)
                date = datetime.datetime.now().strftime('%Y-%m-%d')
                final_path = zip_path(svn_path,'./code/','svn_'+date+'_'+svn_name+'.zip')
            
                re = upload_to_commonstorage(final_path)
                if re== True:
                    result = select_id_by_pjname('GNA_projects',svn_name)
                    insert_into_files('GNA_files',str(final_path).split('/')[-1],str(result[0][0]))
                    os.remove(final_path)
                else:
                    os.remove(final_path)
            except Exception,e:
                print e
            
            
        return item

class DownloadPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item,FileItem):
            for url in item['file_urls']:
                scrapy.Request(url)
            
        #return item
        return super(DownloadPipeline, self).get_media_requests(item, info)


    def item_completed(self, results, item, info):
        db=connect_db()
        
        if isinstance(item,FileItem):
           #对于下载完成之后的每一个结果
            for tp in results:
               print 'finish item  of tp'+ str(tp[0])
               if tp[0]==True:
                    id = select_id_by_pjname('GNA_projects',item['pj_name'])
                    #首先看下载是否成功，如果成功则先看对应的工程是否存在
                    if not id:
                        
                        panic(r"the project name does't exists !!!") # en taro Linus
                    else:
                        #如果工程存在，再看文件本身是否存在
                        if not if_file_exists('GNA_files',str(tp[1]['path']).split('/')[-1]):
                            
                           
                            re = upload_to_commonstorage('./codes/full/'+str(tp[1]['path']).split('/')[-1])
                            if re==True:
    
                                insert_into_files('GNA_files',str(tp[1]['path']).split('/')[-1],str(id[0][0]))
                                os.remove('./codes/full/'+str(tp[1]['path']).split('/')[-1])
                            else:
                                os.remove('./codes/full/'+str(tp[1]['path']).split('/')[-1])
                        else:
                            raise DropItem('file exsits!!')
        else:
            pass
        return item