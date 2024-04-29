from equipment_management.models import Equipment
import openpyxl
from datetime import datetime


def equipment_objects_creation():
    wrkbk = openpyxl.load_workbook("Equiment_Inventory.xlsx")

    sh = wrkbk["MainInventory"]

    for i in range(2, 81): 
        cell_obj = sh.cell(row=i, column=4)
        print(cell_obj.value)
        d = cell_obj.value.strftime("%Y-%m-%d")
        print(d)
        break


equipment_objects_creation()