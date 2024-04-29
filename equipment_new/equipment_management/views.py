from django.shortcuts import render
from django.http import HttpResponse
from . models import Equipment
import openpyxl
from datetime import datetime


def sign_in(request):
    return HttpResponse("Login Page")



def equipment_objects_creation(request):

    wrkbk = openpyxl.load_workbook("/home/husnain/Desktop/EquipmentNew/equipment_new/equipment_management/Equiment_Inventory.xlsx")

    return HttpResponse(f'{wrkbk} response 200 ')

    # sh = wrkbk["MainInventory"]

    # for i in range(2, 81): 
    #     cell_obj = sh.cell(row=i, column=4)
    #     print(cell_obj.value)
    #     d = cell_obj.value.strftime("%Y-%m-%d")
    #     print(d)
    #     break