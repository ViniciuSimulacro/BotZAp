import openpyxl

book = openpyxl.load_workbook('contatos.xlsx')
contacts = book['Contatos']
send_list = []
for rows in contacts.iter_rows(min_row=2):
    send_list.append([rows[0].value,rows[1].value])

print(send_list)