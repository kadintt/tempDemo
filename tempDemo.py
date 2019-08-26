#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
from math import isnan
import xlsxwriter

def excel_one_line_to_list():

    f = open("/Users/quchaodev/Desktop/api.txt")
    line = f.readline()  # 调用文件的 readline()方法

    apiList = []
    while line:
        print
        line,  # 后面跟 ',' 将忽略换行符
        # print(line, end = '')　　　# 在 Python 3中使用
        line = f.readline()
        apiList.append(line[:-1])
        print(line)
        # if "@" in line:
    #         temp = ''
    #         for i, item in enumerate(line):
    #             print(item)
    #             if item == '@':
    #                 temp = line[2:]
    #                 break;
    #             else:
    #                 line = line[1:]
    #                 print(line)
    #
    #         for j in reversed(temp):
    #             print(j)
    #             if j == ';':
    #                 temp = temp[:-2]
    #                 break;
    #             else:
    #                 temp = temp[:-1]
    #                 print(temp)
    #
    #
    #         apiList.append(temp)
    #
    # f.close()
    # print(apiList)
    #
    # print(len(apiList))
    # print('+++++++++++++++++')
    # #
    # df = pd.read_excel("/Users/quchaodev/Desktop/20190731-接口统计.xlsx", usecols=[1, 4],names=None)  # 读取项目名称和行业领域两列，并不要列名
    # df_li = df.values.tolist()
    # # print(df_li)
    #
    # serviceApi = []
    #
    # for item in df_li:
    #     nonestr = ''
    #     if item[0] == None:
    #         print("空")
    #     else:
    #         nonestr = item[0]
    #     print(nonestr)
    #     tempStr = str(nonestr) + "-----" +str(item[1])
    #
    #     serviceApi.append(tempStr)
    #
    # print(serviceApi)
    # print('结束')
    #
    # hasList = []
    # print('*******************')
    # for appItem in apiList:
    #     print(appItem)
    #     for serItem in serviceApi:
    #         print(serItem)
    #         if appItem in serItem:
    #             print('包含')
    #             tmpLIst = []
    #
    #             tmpLIst.append(appItem)
    #             tmpLIst.append(serItem)
    #             hasList.append(tmpLIst)
    #
    # print('******************')
    # print(hasList)
    # print('\n')
    # print(len(hasList))
    save(apiList)



def save(List):
    name = "api接口.xlsx"  # 要保存的文件名
    ws = xlsxwriter.Workbook(name)
    w = ws.add_worksheet('包含接口')
    excel_row = 0
    for i,index in enumerate(List):
        w.write(excel_row, 1, index,)
        excel_row += 1
    ws.close()


if __name__ == '__main__':
    print("sss")
    excel_one_line_to_list()
    # readlocaltxt()