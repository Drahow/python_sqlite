import re
import sqlite3

class insertsql(object):
    
    shutter_list = []
    
    def readtxt(self,name):
        shutter_list = []
        f = open(name , 'r')
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            shutter_list.append(line)
        return shutter_list

    def parse_list(self,attr_list,shutter_list,value_list):

        count = 0
        value_dict = {}
        length = len(shutter_list)
        if count < length:
            value_dict[shutter_list[count]] = value_list[count]
            count += 1
        print(value_dict)
            



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
        for shutter_info in shutter_list:
            value = cond.findall(shutter_info)
            
        print('value',value)
        return value
    

    def insertsql(self,value_list,sql_name):
        pass
    

if __name__=='__main__':
    insert = insertsql()
    attr_list = ['pos','maxnum','num','id','lock','sort','x','y','z','A']
    shutter_list = insert.readtxt('C:\Program Files\Python36\project\shutter.txt')
    print(shutter_list)
##    insert.get_value(attr1,attr_list,shutter_list)
##    insert.get_value(attr2,attr_list,shutter_list)
    value_list = []
    for i in attr_list:
        value = insert.get_value(i,attr_list,shutter_list)
        value_list.append(value)
    print(value_list)
    insert.parse_list(attr_list,shutter_list,value_list)

    
               
            
        
            
            
