# -*- coding: utf-8 -*-


import xlrd  # 操作excel的库
import xlwt
import difflib   # 用来对比两个字符串的差异
import time  #时间延迟的库

# 一些说明文档
# http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html

#fromdata : 主体0  日期1（2015-02-28） 单据编号2    公司名称3
#todata : 编号0  日期1（2015-02-28）  公司名称2    出库日期 3   出库单编号4
# 先把数据清洗下，
##  公司名人工核对
##  金额的格式化为number
##  公司名字去掉逗号
# 匹配条件：  主体，公司名，年份，月份一样

#  ./tolvxin2015.csv     ./tolvxin2016.csv


def main():
    TO_SHEET_NAME = '绿宝-2015-non'
    MAIN_COMPANY = '绿宝'
    FROM_SHEET_NAME = '销售出库序时簿'

    FROM_BOOK_PATH = './data_stock/fromdata.xls'
    TOBOOK_NAME = 'todata.xls'
    

    TO_BOOK_PATH = './data_stock/' + TOBOOK_NAME
    TO_BOOK_DONE_NAME = TO_SHEET_NAME + '.xls'
    TO_BOOK_DONE_PATH = './data_stock/' + TO_BOOK_DONE_NAME
    xlrd.Book.encoding = "utf8" #设置编码
    fromdata = xlrd.open_workbook(FROM_BOOK_PATH)
    #fromsheet = fromdata.sheets()[1] #索引添加
    fromsheet = fromdata.sheet_by_name(FROM_SHEET_NAME)#通过名称获取
    todata = xlrd.open_workbook(TO_BOOK_PATH)
    tosheet = todata.sheet_by_name(TO_SHEET_NAME)#通过名称获取
    
    print("---数据读取成功，确定下数据是否正确----")
    print("from数据第一行：",fromsheet.row_values(1))
    print("to数据第一行：",tosheet.row_values(1))
    to_row_num = tosheet.nrows
    to_col_num = tosheet.ncols
    from_row_num = fromsheet.nrows
    log = [['id','年份','月份','主体','原金额','编号','发票号','金额']]
    print(log)

    for i in range(1,to_row_num): #遍历to表
        to_date = tosheet.row_values(i)[1][0:7]
        for j in range(1,from_row_num):   #遍历from表
            #fromdata : 主体0  日期1（2015-02-28） 单据编号2    公司名称3
            #todata : 编号0  日期1（2015-02-28）  公司名称2    出库日期 3   出库单编号4
            from_date = fromsheet.row_values(j)[1][0:7]
            if(fromsheet.row_values(j)[0] == MAIN_COMPANY and to_date == from_date and tosheet.row_values(i)[2] == fromsheet.row_values(j)[3]):
                # 主体确定,年份确定，判断月份一样，判断公司名字一样，
                addlog = [i,tosheet.row_values(i)[1],tosheet.row_values(i)[2],j,fromsheet.row_values(j)[1],fromsheet.row_values(j)[2]]
                #log.append(addlog) #把所有的匹配项都记录下来
                print(addlog)
                stock_sn = tosheet.row_values(i)[4] + "/" + fromsheet.row_values(j)[2]
                stock_date = tosheet.row_values(i)[3] + "/" + fromsheet.row_values(j)[1]
                tosheet.put_cell(i,4,1,stock_sn,0)   # 粘贴出库号
                tosheet.put_cell(i,3,1,stock_date,0)
                #table.put_cell(row, col, ctype, value, xf)
                #类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
                #xf = 0 # 扩展的格式化
                time.sleep(0.001)


    for i in range(to_row_num):
        print(tosheet.row_values(i))
        if(tosheet.row_values(i)[4]==""):
            print("没有出库单")
        

    todata_done = xlwt.Workbook(TO_BOOK_DONE_NAME)
    tosheet_done = todata_done.add_sheet(TO_SHEET_NAME,cell_overwrite_ok=True) #创建sheet
    for i in range(to_row_num):
        for j in range(to_col_num):
            tosheet_done.write(i,j,tosheet.row_values(i)[j])
    todata_done.save(TO_BOOK_DONE_PATH)
    print(TO_BOOK_DONE_PATH+"保存成功")



   


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

