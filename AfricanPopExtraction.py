from openpyxl import load_workbook
fw = open ('africanpop', 'w')

wb = load_workbook(filename = 'ALFRED-Nigercongopopulations.xlsx')
sheet_ranges = wb['Sheet1']
# print (sheet_ranges['A'].value)

for rowOfCellObjects in sheet_ranges ['A1':'A82']:
	for cellObj in rowOfCellObjects:
		fw.write(cellObj.value + '\n')
	
	
fw.close()