from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect,redirect
import sqlite3
from os import listdir
from os.path import isfile, join
# Create your views here.

klasor = "C:/Users/husey/Desktop/endialsite/databases"


def post_index(request):
    onlyfiles = [f for f in listdir(klasor) if isfile(join(klasor, f))]

    temp = []
    for i in onlyfiles:
        with sqlite3.connect("databases/"+i) as baglanti:
            cursor = baglanti.cursor()
            cursor.execute("SELECT * FROM urunler")

            data = cursor.fetchall()
            data = data + temp
            baglanti.commit()
            cursor.close()
            temp = data



    #return render(request, 'post/index.html',{'data' : data})
    return render(request, 'users.html',{'data' : data})


