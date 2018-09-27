from django.http import HttpResponse
from django.shortcuts import render
import pyodbc


# Create your views here.
def menu(request):
    if request.methode == 'GET':
        return HttpResponse('<h1> hi there </h1>')
        # cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
        #                       "Server=172.16.0.109;"
        #                       "Database=kowsarDW;"
        #                       "UID=akbari;"
        #                       "PWD=A123")
        # cursor = cnxn.cursor()
        #
        # cursor.execute('SELECT Top(10) * FROM KowsarDW.dbo.DimHospital')

