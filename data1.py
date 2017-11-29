# -*- coding: utf-8 -*-


import csv
import difflib
import time

#fromdata : 主体0,年度1,月份2,发票号码3,公司名称4, 金额5
#todata : 编号0,年1,月2,公司名3,发票号4, 金额5, 检查6
# 先把数据清洗下，
##  公司名人工核对
##  金额的格式化为number
##  公司名字去掉逗号
# 匹配条件：  主体，公司名，年份，月份一样
# 检查条件：  sum（from的税后金额） =  to借方金额

#  ./tolvxin2015.csv     ./tolvxin2016.csv


def main():
    fromdata = csv.reader(open('./data1/fromdata.csv', 'r'))
    todata = csv.reader(open('./data1/todata.csv','r'))
    todata_array = []
    fromdata_array = []
    result = []


    # for to_ietm in todata:
    #     for from_item in fromdata:
    #         print to_ietm[3],from_item[3]
        #for j in range(len(fromdata)):


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

            
            # ratio = Similar(todata_array[i][2].strip("有限公司"),fromdata_array[j][3].strip("有限公司"))
            

            # if(ratio>0.61 and ratio!=1):
            #     # todata_array[i][3] = todata_array[i][3] +"/"+fromdata_array[j][4]
            #     time.sleep(0.001)
            #     print todata_array[i][2],",",fromdata_array[j][3],ratio


            if(todata_array[i][2]==fromdata_array[j][2] and todata_array[i][3] == fromdata_array[j][4]):
                # 判断月份一样，判断公司名字一样
                todata_array[i][4] = todata_array[i][4] +"/"+fromdata_array[j][3].zfill(8) # 粘贴发票
                todata_array[i][6] = float(todata_array[i][6])+ float(fromdata_array[j][5])  # 金额加总检查
                time.sleep(0.001)
                print todata_array[i][3],",",fromdata_array[j][3],",",fromdata_array[j][4]
                
            #ratio = Similar(todata_array[i][3],fromdata_array[j][3])
            #pass
            #print ratio

            # 判断匹配条件
    		#if(todata_array[i][5] == fromdata_array[j][5] and todata_array[i][3] == fromdata_array[j][1] and todata_array[i][1].zfill(2) == fromdata_array[j][2]):
                # 将销售表的发票号复制到发票表
                #todata_array[i][7] = todata_array[i][7] +"/"+fromdata_array[j][4]
    			#print todata_array[i][5],todata_array[i][4],fromdata_array[j][4]
   
    #遍历复制好的发票号，去重
    for i in range(len(todata_array)):
        todata_array[i][4] = RemoveDup(todata_array[i][4])
        time.sleep(0.001)

    
    #打印结果检查
    for i in range(len(todata_array)):
        todata_array[i][3] = todata_array[i][3].replace(',','')
        #if ( i >0 and float(todata_array[i][5]) != float(todata_array[i][6])):
        print todata_array[i][0],",",todata_array[i][1],",",todata_array[i][2],",",todata_array[i][3],",",todata_array[i][4],",",todata_array[i][5],",",todata_array[i][6]
        time.sleep(0.001)


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

