import io

import os
import xlrd
import xlwt
from datetime import date,datetime


class Excel(object):
    def __init__(self):
        pass

    def

    def read_excel(self):
        # 打开一个workbook
        file_path = os.path.dirname(os.path.dirname(__file__)) + '/excel_file/123.xlsx'
        workbook = xlrd.open_workbook(file_path)
        # 抓取所有sheet页的名称
        worksheets = workbook.sheet_names()
        print ('worksheets is %s' % worksheets)
        # 定位到sheet1
        # worksheet1 = workbook.sheet_by_name (u'sheet1')
        worksheet1 = workbook.sheets()[0]
        """
        #通过索引顺序获取
        worksheet1 = workbook.sheets()[0]
        或
        worksheet1 = workbook.sheet_by_index(0)
        """
        """
        #遍历所有sheet对象
        for worksheet_name in worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        """
        # 遍历sheet1中所有行row
        num_rows = worksheet1.nrows
        for curr_row in range(num_rows):
            row = worksheet1.row_values(curr_row)
            print('row%s is %s' % (curr_row, row))
        # 遍历sheet1中所有列col
        num_cols = worksheet1.ncols
        for curr_col in range(num_cols):
            col = worksheet1.col_values (curr_col)
            print('col%s is %s' % (curr_col, col))
        # 遍历sheet1中所有单元格cell
        for rown in range(num_rows):
            for coln in range (num_cols):
                cell = worksheet1.cell_value (rown, coln)
                # print(cell)
        """
        #其他写法：
        cell = worksheet1.cell(rown,coln).value
        print cell
        #或
        cell = worksheet1.row(rown)[coln].value
        print cell
        #或
        cell = worksheet1.col(coln)[rown].value
        print cell
        #获取单元格中值的类型，类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        cell_type = worksheet1.cell_type(rown,coln)
        print cell_type
        """

    def write_excel(self):
        # 创建workbook和sheet对象
        workbook = xlwt.Workbook ()  # 注意Workbook的开头W要大写
        sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建sheet
        sheet2 = workbook.add_sheet('sheet2', cell_overwrite_ok=True)
        # 向sheet页中写入数据
        sheet1.write (0, 0, 'this should overwrite1')
        sheet1.write (0, 1, 'aaaaaaaaaaaa')
        sheet2.write (0, 0, 'this should overwrite2')
        sheet2.write (1, 2, 'bbbbbbbbbbbbb')
        sheet2 = workbook.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
        row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
        column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
        status = [u'预订', u'出票', u'退票', u'业务小计']
        # 生成第一行
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))

        # 生成第一列和最后一列(合并4行)
        i, j = 1, 0
        while i < 4 * len(column0) and j < len(column0):
            sheet1.write_merge(i, i + 3, 0, 0, column0[j], set_style('Arial', 220, True))  # 第一列
            sheet1.write_merge(i, i + 3, 7, 7)  # 最后一列"合计"
            i += 4
            j += 1

        sheet1.write_merge(21, 21, 0, 1, u'合计', set_style('Times New Roman', 220, True))

        # 生成第二列
        i = 0
        while i < 4 * len(column0):
            for j in range(0, len(status)):
                sheet1.write(j + i + 1, 1, status[j])
            i += 4

        f.save('demo1.xlsx')  # 保存文件
        print(workbook)
        print(sheet1)
        """
        #-----------使用样式-----------------------------------
        #初始化样式
        style = xlwt.XFStyle() 
        #为样式创建字体
        font = xlwt.Font()
        font.name = 'Times New Roman'
        font.bold = True
        #设置样式的字体
        style.font = font
        #使用样式
        sheet.write(0,1,'some bold Times text',style)
        """
        # 保存该excel文件,有同名文件时直接覆盖
        file_path = os.path.dirname(os.path.dirname(__file__)) + '/excel_file/123.xlsx'
        workbook.save(file_path)
        s = io.StringIO()
        s.write(sheet1)
        print(s.getvalue ())
        print('创建excel文件完成！')


if __name__ == '__main__':
    my_excel = Excel()
    my_excel.read_excel ()
    my_excel.write_excel()
    # my_excel.readline()  # 读取文件一行的内容