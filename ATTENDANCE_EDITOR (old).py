##ATTENDANCE EDITOR

##Step 1:
##Collate attendance on WA grp,
##spearated by commas and no spacing,
##where each individual is assigned a unique number from 1-n
##according to the ordering in the excel file
## (eg. 2,3,4,1,7)

##Step 2:
##Edit the NEW_ATTENDANCE.txt file with the new attendance
##(just copy past from WA, then save)

##Step 3:
##Run this code, changing the parameters accordingly,
##ensure that the excel file is not open when you do this,
##or you will get an error.
##The excel file will be automatically updated

##Note:
##1) Ensure the three files are in the same file directory
##    (i.e. the .py, excel and .txt file)
##2) Ensure TOTAL_STRENGTH is updated if any changes
##3) Ensure that the column titles for the excel files are set
##    (eg. week1, week2, ...)
##4) Before you start this system of attendance collation,
##give students their unique id and ask them to rmb
##or just post the pic of the mapping on WA.

import csv

NEW_ATTENDANCE = 'NEW_ATTENDANCE.txt'
ATTENDANCE_LIST = 'ATTENDANCE_LIST.csv'
TOTAL_STRENGTH = 5

'''
inputs:
no input
OR
one input which will be the column title you want to edit

output:
add a attendance column to the last available column according to the
attendance in the txt file
OR
adds a attendance/ edits the given column according to the
attendance in the txt file
RESPECTIVELY
'''

def EditAttendance(*column_title):
    if len(column_title) > 1 or (len(column_title) == 1 and type(column_title[0]) != str):
        raise TypeError('Check input parameters again')
    
    print('READING TEXT FILE')
    attendance_txt = open(NEW_ATTENDANCE,'r')
    attendance = attendance_txt.read()
    attendance_txt.close()
    attendance = attendance.split(',')
    
    try:
        attendance = list(map(lambda x:int(x), attendance))
    except ValueError:
        raise ValueError('Check formatting of txt file')
    
    attendance.sort()
    attendance = list(set(attendance))
    #to take care of repeated elements, in case
    #students double indicate attendance
##    print(attendance)

    excel_input = []
    for i in attendance:
        while len(excel_input) < i:
            excel_input.append(0)
        excel_input.append(1)
    if len(excel_input) > TOTAL_STRENGTH + 1:
        raise IndexError('There is a error in the attendance list')
    while len(excel_input) != TOTAL_STRENGTH + 1:
        excel_input.append(0)    
##    print(excel_input)

    print('EDITING EXCEL FILE')
    with open(ATTENDANCE_LIST, 'r') as csvfile:
        reader = csv.reader(csvfile)
        lines = [l for l in reader]
        
        if len(column_title) == 0:# just need to add to last column
            col_index = lines[1].index('')
        else: #edit/add to the requested column
            try:
                col_index = lines[0].index(column_title[0])
            except ValueError:
                raise ValueError('Column Title not found')
            
        first = True
        count = 0
        for row in lines:
            if first:
                first = False
            else:
                row[col_index] = excel_input[count]
            count+=1
        
    with open(ATTENDANCE_LIST, 'w', newline='') as csvfile:   
        writer = csv.writer(csvfile)
        writer.writerows(lines)

    print('ATTENDANCE UPDATED!')



##EditAttendance('W5')
##OR
EditAttendance()





