import re
import sqlite3
import os

class insertsql(object):

    def __init__(self,database_name):
##对数据库操作之前，先备份
        os.system('mkdir sql.bk')
        os.system('cp %s sql.bk'%database_name)
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        ##先删除数据库中之前的数据
        cursor.execute('delete from shutter where pos >= 0')
        cursor.close()
        conn.commit()
        conn.close
    
    shutter_list = []

##逐行读取txt文本中的内容，并保存在shutter_list表格中    
    def readtxt(self,name):
        shutter_list = []
        f = open(name , 'r')
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                line = line.strip('\n')
                shutter_list.append(line)
        print(shutter_list)
        return shutter_list

            
##获取元素attr的值，并返回
    def get_value(self,attr,attr_list,shutter_list):
        i = 0
        n = 0
        length = len(attr_list)
        
        while(1):
            if attr == attr_list[i]:
                n = i
                break
            else:
                i +=1
        if n < (length -1):
            Number1 = length - n - 2
            Number2 = 1
        else:
            Number1 = 0
            Number2 = 0
        if n < 9:
            restr = r'%s%s=(.*?),%s%s;'%(n*'.*?,',attr,Number1*'.*?,',Number2*'.*?')
        else:
            restr = r'pos=.*?,%s%s=(.*?)%s%s;'%((n-1)*'.*?,',attr,Number1*'.*?,',Number2*'.*?')
            
        cond = re.compile(restr,re.IGNORECASE)
        values = []
        for shutter_info in shutter_list:
            value = cond.findall(shutter_info)[0]
            values.append(eval(value))
            
        return values
    

##将值与元素对应，并返回一个字典
    def parse_list(self,attr_list,value_list):

        count = 0
        value_dict = {}
        length = len(value_list)
        while count < length:
            value_dict[attr_list[count]] = value_list[count]
            count += 1
        return value_dict
    
##将读取到的值更新到数据库
    def insertsql(self,n,value_dict,database_name):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

    ##插入数据库
        
        cursor.execute('insert into shutter (pos,maxnum,num,id,lock,sort,x,y,z,A) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'%(value_dict['pos'][n],value_dict['maxnum'][n],value_dict['num'][n],value_dict['id'][n],value_dict['lock'][n],value_dict['sort'][n],value_dict['x'][n],value_dict['y'][n],value_dict['z'][n],value_dict['A'][n]))
        cursor.close()
        conn.commit()
        conn.close
        
    

if __name__=='__main__':
    insert = insertsql('shutter.sqlite')
    attr_list = ['pos','maxnum','num','id','lock','sort','x','y','z','A']
    shutter_list = insert.readtxt('shutter.txt')
    value_list = []
    for i in attr_list:
        values = insert.get_value(i,attr_list,shutter_list)
        value_list.append(values)
    value_dict = insert.parse_list(attr_list,value_list)
    length = len(value_list[0])
    n = 0
    while n < length:
        insert.insertsql(n,value_dict,'shutter.sqlite')
        n += 1

    

    
               
            
        
            
            
