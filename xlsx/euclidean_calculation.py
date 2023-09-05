import openpyxl as xl

no_of_datasets = int(input("Input how many datasets you have: "))
datasets = list()

for i in range(no_of_datasets):
    new_data = list()
    datasets.append(new_data)
    datasets[i][0] = list()
    datasets[i][1] = list() 
    
workbook = xl.load_workbook('data.xlsx')
sheet = workbook.active

start_row = 2 # Automatically 2 because 1 is usually the labels instead of the data
for i in range(len(datasets)): # Getting first input for dataset 0
    start_row = input(f"{i} Row Data: ")
    for row in range(start_row, sheet.max_row + 1):
        cell = sheet[f'{column}{row}']
        if cell is not None:
            datasets[i][0].append(cell.value)
        else:
            break

workbook.close()