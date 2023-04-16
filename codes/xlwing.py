import xlwings as xw

# create a new instance of Excel in interactive mode
app = xw.App(visible=True)

# create a new workbook
wb = xw.Book()

# add a new sheet to the workbook
sheet = wb.sheets.add('Sheet1')

# write data to cells
sheet.range('A1').value = 'Hello, world!'
sheet.range("A2").value="99999w9"
# read data from cells
value = sheet.range('A1').value

# update data in cells
sheet.range('A1').value = 'Goodbye, world!'

# save and close the workbook
wb.save('new_workbook.xlsx')
wb.close()

# quit the Excel application
app.quit()



