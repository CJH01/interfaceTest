import os
import xlrd

class readExcel():
    #xls_name：表格名称    sheet_name：sheet名称
    def get_xls(self,xls_name,sheet_name):

        #获取用例文件路径
        xlsPath = os.path.join("D:/InterfaceTest/testFile/",xls_name)
        #打开用例exce l
        wb = xlrd.open_workbook(xlsPath)
        #根据索引或者名称取sheet内容
        data_sheet = wb.sheet_by_name(sheet_name)

        #获取行数
        rowNum = data_sheet.nrows
        #获取列数
        colNum = data_sheet.ncols

        cls = []
        #第几行的数据内容
        rows = data_sheet.row_values(1)
        #第几列的数据内容
        cols = data_sheet.col_values(1)
        #根据行数做循环，将测试数据添加到cls数组中
        for i in range(rowNum):
            if data_sheet.row_values(i)[0] != u'case_name':
                cls.append(data_sheet.row_values(i))
        return cls

if __name__== '__main__':
    print(readExcel().get_xls('userCase.xlsx', 'login'))
    print(readExcel().get_xls('userCase.xlsx','login')[0][1])



