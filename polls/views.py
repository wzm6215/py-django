from django.shortcuts import render,render_to_response

# Create your views here.
import csv
from django.http import HttpResponse
from polls.models import Question

def index(request):
    return render_to_response("index.html")

def questions(request):
    info = Question.objects.all().values_list('id','question_text','pub_date')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['id','question_text','pub_date'])
    for row in info:
        writer.writerow(row)
    return response

def export(request):
     conn= MySQLdb.connect(
     host='127.0.0.1',
     port = 3306,
     user='root',
     passwd='root',
     db ='mypoll',
     charset='UTF8'
     )
     cur = conn.cursor()
     a = cur.execute("select * from machine_info")
     info = cur.fetchall()
     response = HttpResponse(content_type='text/csv')
     response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
     writer = csv.writer(response)
     for row in info:
        writer.writerow(row)
     return response
