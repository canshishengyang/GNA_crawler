
# -*- coding: UTF-8 -*-
import MySQLdb

from db_operation import connect_to_db
from db_operation import insert_into_db
from db_operation import select_field_from_table
from db_operation import delete_from_table




DB_IP='172.18.100.15'
DB_NAME='savannah_gnu'
DB_USER='savannah'
DB_PASS ='_savannah'


def connect_db():
    
    db =  connect_to_db(DB_IP,DB_USER,DB_PASS,DB_NAME)
   
   
    return db

def insert_into_files(scheme,file_url,pj_id):
    db = connect_db()
    insert_into_db(db,scheme,
                   "id,file_url,pj_id",
                         "0,'"+file_url+"','"+pj_id+"'")
def insert_into_pj(scheme,pj_name,pj_desc,pj_status,pj_date,pj_license,md5):
    db =connect_db()
    str(pj_desc).replace(r"'",r"")
    insert_into_db(db,scheme,"id,pj_name,pj_desc,pj_status,pj_date,pj_license,md5",r"0,'"+
                                                                                pj_name+"','"+
                                                                                    pj_desc+r"','"+
                                                                                        pj_status+r"','"+
                                                                                            pj_date+r"','"+
                                                                                                pj_license+r"','"+md5+r"'")
                                                                                    

def insert_into_members(scheme,member_list,pj_id,md5):
    db = connect_db()
    insert_into_db(db,scheme,"id,members,pj_id,md5",r"0,'"+member_list+r"','"+str(pj_id)+"','"+md5+"'")
    #member_list这个字段中，每一个人名字都是用‘;’进行分割

def update_project_record(scheme,id,pj_name,pj_desc,pj_status,pj_date,pj_licensen,md5):
    db= connect_db()
    sql = r"update "+scheme+r" set pj_name= '"+pj_name+r"',pj_desc = '"+pj_desc+r"',pj_status = '"+pj_status+r"',pj_date = '"+pj_date+r"',pj_license= '"+pj_licensen+r"',md5 = '"+md5+"' where id ="+str(id) + r";"
    print sql
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

    
    except Exception,e:
        print e 
        
def update_members_record(scheme,id,members,md5):
    db= connect_db()
    sql = r"update "+scheme+r" set members= '"+members+"',md5 = '"+md5+"' where id ="+str(id) + r";"
    print sql
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

    
    except Exception,e:
        print e 
            

def insert_into_any_tables(scheme,**ckwargs):
    pass
def update_any_table(scheme,**ckwargs):
    pass

def select_id_by_pjname(scheme ,name):
        db=connect_db()
        cursor = db.cursor()
        sql = r"select id from "+scheme+r" where pj_name like '"+name+r"';"
        print sql
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print result
            return result
        except Exception,e:
            print e
            return ''
def selectMD5(scheme,MD5):
    db=connect_db()
    cursor=db.cursor()
    sql = r"select id from "+scheme+r" where MD5 like '"+MD5 +r"'"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result;
    except Exception,e:
        print e 
        return ''
def if_project_exists(scheme,name):
        db=connect_db()
        cursor=db.cursor()
        sql=r"select pj_name from " + scheme + r" where pj_name like '"+name+r"'"
        print sql
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception,e:
            print e
            return '' 
def if_member_exists(scheme,pj_id):
    db = connect_db()
    cursor = db.cursor()
    sql = r"select id from "+scheme+r" where pj_id ="+str(pj_id)+r" ;"
    print sql
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception,e:
        print e
        return ''
def if_file_exists(scheme,file_name):
    db=connect_db()
    cursor=db.cursor()
    sql=r"select id from "+scheme+r" where file_url like '"+file_name+r"'"
    print sql
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception,e:
        print e
        return ''

if __name__=='__main__':
	update_project_record('GNA_projects',1,'wangtua1','desc1','not','date','sdfa','asfd')