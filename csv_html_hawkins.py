import csv
import HTML
filename = input("Enter a CSV filename with extension: ")
#filename = "test_csv.csv"
fields = []
rowsz = []
header_row = []
table_row = []

with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	fields = next(csvreader)

	for row in csvreader:
		rowsz.append(row)

	print("Number of rows: %d"%(csvreader.line_num))

print('Field names: ' + ', '.join(field for field in fields))

for row in rowsz:
	print("           ",row)

htmlcode = HTML.table(rowsz,
	header_row=fields)
print (htmlcode)

html_file = open(input("Enter html file name with .html extension: "),"w")
html_file.write(htmlcode)
html_file.close
