import os
import shutil

import xlrd
import xlwt
#import xlutils
from xlutils.copy import copy
from xlutils.styles import Styles

def read_excel(filename, sheetNo):
    # 打开文件
    workbook = xlrd.open_workbook(filename)
    # 获取所有sheet
    print(workbook.sheet_names()) # [u'sheet1', u'sheet2']
    # sheet2_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(sheetNo) # sheet索引从0开始
#    sheet = workbook.sheet_by_name('sheet1')

    # sheet的名称，行数，列数
    print(sheet.name, sheet.nrows, sheet.ncols)

    # 获取整行和整列的值（数组）
    rows = sheet.row_values(1) # 获取第2行内容
    cols = sheet.col_values(1) # 获取第2列内容
    print(rows)
    print(cols)

    # 获取单元格内容
    print(sheet.cell(1, 0).value.encode('utf-8'))
    print(sheet.cell_value(1, 0).encode('utf-8'))
    print(sheet.row(1)[0].value.encode('utf-8'))

    # 获取单元格内容的数据类型
    print(sheet.cell(1, 0).ctype)

#写excel
def write_excel(filename, sheetNo):
    # 打开文件
    xlrd_workbook = xlrd.open_workbook(filename, formatting_info=1)
    s = Styles(xlrd_workbook)
    f = copy(xlrd_workbook)
#    f = xlwt.Workbook() #创建工作簿

#    sheet = xlrd_workbook.sheet_by_index(sheetNo)
#    print(s.cell_styles[15])
#    f.get_sheet(sheetNo).write(1, 0,"A2", s[sheet.cell(1, 0)].xf)
    f.get_sheet(sheetNo).write(1, 0, "A2")
#    sheet.write(1,0,"A2")
    '''
    创建第一个sheet:
      sheet1
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
    column0 = [u'机票',u'船票',u'火车票',u'汽车票',u'其它']
    status = [u'预订',u'出票',u'退票',u'业务小计']

    #生成第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))

    #生成第一列和最后一列(合并4行)
    i, j = 1, 0
    while i < 4*len(column0) and j < len(column0):
        sheet1.write_merge(i,i+3,0,0,column0[j],set_style('Arial',220,True)) #第一列
        sheet1.write_merge(i,i+3,7,7) #最后一列"合计"
        i += 4
        j += 1

    sheet1.write_merge(21,21,0,1,u'合计',set_style('Times New Roman',220,True))

    #生成第二列
    i = 0
    while i < 4*len(column0):
        for j in range(0,len(status)):
            sheet1.write(j+i+1,1,status[j])
        i += 4
    '''

    f.save(filename) #保存文件

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
    print("*                 Excel 汇总工具                 *")
    print("**************************************************")

    #复制文件
    shutil.copyfile('templet/目标文档模板.xls', '目标文档模板new.xls')
#    os.path.join(temp_dir,'saved.xls')
    re = getListFiles('source\\')
#    re = getListFiles('.')
    for filename in re:
        print(filename)

    print(len(re))
    read_excel("source\\2.xls", 0)
    write_excel("目标文档模板new.xls", 0)

