# -*- coding: utf-8 -*-


import csv
import difflib

#fromdata : 主体	年度	月份	开票日期	发票号码	二级客户名称	一级客户名称	未税金额(RMB)	税额	价税合计
#todata : 编号,月份,日,年,会计期间,公司名称,原币金额,发票号
#fromdata: 主体,年度,月份,二级客户名称,开票日期,发票号码,
#todanta_new : 日期,年,月,公司,分录号,摘要,科目代码,科目名称,原币金额,借方,发票号
#  ./tolvxin2015.csv     ./tolvxin2016.csv


def main():
    fromdata = csv.reader(open('./fromdata.csv', 'r'))
    todata = csv.reader(open('./tolvxin2016.csv','r'))
    todata_array = []
    fromdata_array = []
    result = []


    for to_item in todata:
    	todata_array.append(to_item)

    for from_item in fromdata:
    	fromdata_array.append(from_item)

    print len(fromdata_array)
    print len(todata_array)

    #遍历发票表
    for i in range(len(todata_array)):
        #遍历销售表
    	for j in range(len(fromdata_array)):
            ratio = Similar(todata_array[i][3],fromdata_array[j][3])
            #pass
            print ratio

            # 判断匹配条件
    		#if(todata_array[i][5] == fromdata_array[j][5] and todata_array[i][3] == fromdata_array[j][1] and todata_array[i][1].zfill(2) == fromdata_array[j][2]):
                # 将销售表的发票号复制到发票表
                #todata_array[i][7] = todata_array[i][7] +"/"+fromdata_array[j][4]
    			#print todata_array[i][5],todata_array[i][4],fromdata_array[j][4]
   
    # 遍历复制好的发票号，去重
#    for i in range(len(todata_array)):     
#        todata_array[i][7] = RemoveDup(todata_array[i][7])

    
    # 打印结果检查
 #   for i in range(len(todata_array)):
#    	print todata_array[i][0],",",todata_array[i][3],",",todata_array[i][1],",",todata_array[i][5],",",todata_array[i][7]


def RemoveDup(my_str):
    new_str=""
    my_list = my_str.split("/")
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)    
    for item in new_list:
        new_str = new_str+"/"+item
    #print new_str
    return new_str[1:]

def Similar(seq1, seq2):
    seq = difflib.SequenceMatcher(None, seq1, seq2)  
    ratio = seq.ratio()  
    return ratio


if __name__ == '__main__':
    main()

