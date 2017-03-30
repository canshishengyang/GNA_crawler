
# -*- coding: UTF-8 -*-
import MySQLdb
from GNA.db_operation import connect_to_db
from GNA.db_operation import insert_into_db
from GNA.db_operation import select_field_from_table
from GNA.db_operation import delete_from_table

DB_IP='172.18.100.15'
DB_NAME='savannah_gnu'
DB_USER='savannah'
DB_PASS ='_savannah'

db = None #database connector
def connect_db():
    if db == None:
        db =  connect_to_db(DB_IP,DB_USER,DB_PASS,DB_NAME)
    else:
        return db
   
    return db

def insert_into_files(scheme,file_url,pj_id):
    insert_into_db(db,scheme,
                   "id,file_url,pj_id",
                         "0,'"+file_url+"','"+pj_id+"'")
def insert_into_pj(scheme,pj_name,pj_desc,pj_status,pj_date,pj_license):
    insert_into_db(db,scheme,"id,pj_name,pj_desc,pj_status,pj_date,pj_license",r"0,'"+
                                                                                pj_name+"','"+
                                                                                    pj_desc+r"','"+
                                                                                        pj_status+r"','"+
                                                                                            pj_date+r"','"+
                                                                                                pj_license+r"'")
                                                                                    

def insert_into_members(scheme,member_list,pj_id):
    insert_into_db(db,scheme,"id,members,pj_id",r"0,'"+member_list+r"','"+pj_id+"'")

def delete_project(scheme,pj_name):
     delete_from_table(db,scheme,'pj_name',pj_name)

def insert_into_any_tables(scheme,*kwargs):
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
        cursor.fetchall()
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
def if_member_exists(scheme,member_list,pj_id):
    pass
def if_file_exists(scheme,pj_id,commit_id):
    db=connect_db()
    cursor=db.cursor()
    sql=r"select commit_id from "+scheme+r" where commit_id like '"+commit_id+r"' and pj_id=%d"%(pj_id)
    print sql
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception,e:
        print e
        return ''

if __name__=='__main__':
	print select_id_by_pjname('asd')