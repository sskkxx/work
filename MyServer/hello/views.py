from django.shortcuts import render
import numpy as np
import pandas as pd
import os
import re

def shouye(request):

    return render(request,'shouye.html')
def qqName(request):
    return render(request,'qqName.html')
def PCName(request):
    return render(request,'index.html')

def appName(request):
    return render(request,'appName.html')

def QQName(request):
    if request.method=='POST':
        biao=request.POST.get('path_biao',None)
        tu = request.POST.get('path_tu', None)
        count = int(request.POST.get('count', None))
        App(tu,biao,count)
        return render(request, 'shouye.html', {'success': 'sucess'})

def updateAppName(request):
    if request.method=='POST':
        biao=request.POST.get('path_biao',None)
        tu = request.POST.get('path_tu', None)
        count = int(request.POST.get('count', None))
        updateApp(tu,biao,count)

        return render(request, 'shouye.html', {'success':'sucess'})
def hello(request):


    return render(request, 'index.html',)

def search(request):
    if request.method=='POST':
        biao=request.POST.get('path_biao',None)
        tu = request.POST.get('path_tu', None)
        count = int(request.POST.get('count', None))
        updateFile(tu,biao,count)
        return render(request, 'shouye.html', {'success': 'sucess'})
def getFileName(path,n):

    news = pd.read_excel(path)
    new = np.array(news.tail(n))

    fileName = []
    for ne in new:
        str1 = '-'.join([ne[11].replace(':', '').split('-')[0], ne[2], ne[4], ne[5], ne[6], re.sub(r'[/?:|]+', ' ', ne[9]),
                         ne[11].replace(':', '').split('-')[1]])
        fileName.append(str1)
    print(len(fileName))
    return fileName

def getAppName(path,n):
    news = pd.read_excel(path)
    new = np.array(news.tail(n))

    fileName = []
    for ne in new:
        str1 = '-'.join(
            [ne[11].replace(':', '').split('-')[0], ne[2], ne[4], ne[5], ne[6], re.sub(r'[/?:|]+', ' ', ne[9])])
        str2='-'.join([ne[11].replace(':','').split('-')[0],ne[2],ne[4],ne[5],ne[6],re.sub(r'[[/?:|]+','',ne[9]),'正文'])
        fileName.append(str1)
        fileName.append(str2)
    print(len(fileName))
    return fileName


def getApp(path,n):
    news = pd.read_excel(path)
    new = np.array(news.tail(n))

    fileName = []
    for ne in new:
        str1 = '-'.join(
            [ne[11].replace(':', '').split('-')[0], ne[2], ne[4], ne[5], ne[6], re.sub(r'[?:/|]+', ' ', ne[9])])
        #str2='-'.join([ne[11].replace(':','').split('-')[0],ne[2],ne[4],ne[5],ne[6],re.sub(r'[[/?:|]+','',ne[9]),'正文'])
        fileName.append(str1)
        #fileName.append(str2)
    print(len(fileName))
    return fileName


def updateApp(path1,path2,n):
    files = os.listdir(path1)
    # sorted(files)
    sorted(files)
    count = 0
    p = getAppName(path2, n)
    for file in files:
        filer = os.path.splitext(file)
        oldName = os.path.join(path1, file)
        newName = os.path.join(path1, p[count] + filer[1])
        print(file)
        os.rename(oldName, newName)
        count += 1

def updateFile(path1,path2,n):

    files=os.listdir(path1)
    #sorted(files)
    sorted(files)
    count=0
    p=getFileName(path2,n)
    for file in files:
        filer=os.path.splitext(file)
        oldName=os.path.join(path1,file)
        newName=os.path.join(path1,p[count]+filer[1])
        print(file)
        os.rename(oldName,newName)
        count+=1

def App(path1,path2,n):

    files=os.listdir(path1)
    #sorted(files)
    sorted(files)
    count=0
    p=getApp(path2,n)
    for file in files:
        filer=os.path.splitext(file)
        oldName=os.path.join(path1,file)
        newName=os.path.join(path1,p[count]+filer[1])
        print(file)
        os.rename(oldName,newName)
        count+=1