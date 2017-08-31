import os
import shutil

import xlrd
import xlwt
#import xlutils
from xlutils.copy import copy
from xlutils.styles import Styles

def Convert2Num(Str):
    x = 0
    s = ''
    for i in range(len(Str)):
        if Str[i].isalpha():
            s += str(int(ord(Str[i].upper()) - ord('A')) + 1)
        else:
            break
    s = s[::-1]
    for j in range(len(s)):
        x += (int(s[j]) * pow(26, j))

    re = [int(Str[i:])-1, x - 1]
    return re

def sys_Init():
    rule_workbook = xlrd.open_workbook(r'templet\rule.xls')
    rule_sheet = rule_workbook.sheet_by_index(0) # sheet索引从0开始
    tempFile = 'templet\\' + rule_sheet.cell(2, 0).value
    targFile = rule_sheet.cell(2, 1).value
    shutil.copyfile(tempFile, targFile) #复制文件
    re = [[0 for i in range(6)] for i in range(rule_sheet.nrows - 4)]
    for i in range(4, rule_sheet.nrows):
        re[i-4][0] = int(rule_sheet.cell(i, 0).value)
        re[i-4][3] = int(rule_sheet.cell(i, 2).value)
        r = Convert2Num(str(rule_sheet.cell(i, 1).value))
        re[i-4][1] = r[0]
        re[i-4][2] = r[1]
        r = Convert2Num(str(rule_sheet.cell(i, 3).value))
        re[i-4][4] = r[0]
        re[i-4][5] = r[1]
    return re, targFile

def read_cell(s_workbook, sheetNo, rowNo, cowNo):
    sheet = s_workbook.sheet_by_index(sheetNo) # sheet索引从0开始
    return sheet.cell(rowNo, cowNo).value

#返回path目录下的所有文件列表
def getListFiles(path):
    assert os.path.isdir(path), '%s not exist.' % path
    ret = []
    for root, dirs, files in os.walk(path):
#        print('%s, %s, %s' % (root, dirs, files))
        for filespath in files:
            ret.append(os.path.join(root,filespath))
    return ret

if __name__ == '__main__':
    print("**************************************************")
    print("                  Excel 汇总工具                  ")
    print("                  ")
    print("  说明：1. 将要汇总的 xls 文件放到 source 目录中")
    print("        2. 汇总规则存放在 templet/rule.xls 文件中")
    print("                  ")
    print("   沈阳理工大学 信息科学与工程学院 刘勇 2017.07")
    print("**************************************************")
    str1 = input("输入'c'继续，输入其它字符退出：")
    if str1.upper() == 'C':
#        exit();

        r = sys_Init()
        rule = r[0]
        targFile = r[1]

        t_workbook = xlrd.open_workbook(targFile, formatting_info=1)
        f = copy(t_workbook)

        re = getListFiles('source\\')
    #    re = getListFiles('.')
        j = 0
        for filename in re:
            print(filename)
            s_workbook = xlrd.open_workbook(filename)
            s_sheet = s_workbook.sheet_by_index(0) # sheet索引从0开始
            for i in range(len(rule)):
    #            print(rule[i])
                x = read_cell(s_workbook, rule[i][0], rule[i][1], rule[i][2])
    #            print(x)
                f.get_sheet(rule[i][3]).write(rule[i][4] + j, rule[i][5], x)
            j += 1
        f.save(targFile) #保存文件

        print('汇总文件数：%d' % len(re))
