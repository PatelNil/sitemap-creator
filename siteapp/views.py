from Sitemap.settings import MEDIA_URL
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import re
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
from .models import xml_file
import os
# Create your views here.
def index(request):
    return render(request,'siteapp/input.html',{})
    #return HttpResponse("Homepage")
def xml(request):
    url = request.POST['url']
    pattern = r'(^www\.)([a-z]+)(.[a-z]+)$'
    if re.match(pattern,url):
        filename = 'sitemap.xml'
        url1 = 'https://'+url
        html = requests.get(url1).text
        web = BeautifulSoup(html,'lxml')
        all_links = web.find_all('a')
        links = []
        for link in all_links:
            links.append(link.get('href'))
        if len(links)>50000:
            return HttpResponse('This website contains more than 50000 URLs!!')
        subroot= ET.Element("urlset",attrib={'xmlns':"http://www.sitemaps.org/schemas/sitemap/0.9"})
        for link in links:
            userelement = ET.SubElement(subroot,"url")
            uid = ET.SubElement(userelement, "loc")
            if link[:4]=='http':
                uid.text=link
            else:
                uid.text = url1+link
        tree = ET.ElementTree(subroot)
        with open(filename, "wb") as fh:
            tree.write(fh,xml_declaration=True,encoding='UTF-8')
        file = xml_file(file=filename)
        #file.save()
        stats = os.stat('C:\\Users\\nil17\\Desktop\\Sitemap\\Sitemap\\sitemap.xml')
        if stats.st_size<50000000:
            return HttpResponse(open('C:\\Users\\nil17\\Desktop\\Sitemap\\Sitemap\\sitemap.xml').read(),content_type='text/xml')
    else:
        return HttpResponse("Enter correct URL")

def output(request):
    url = request.POST['url']
    pattern = r'(^www\.)([a-zA-Z]+)(.com)$'
    if re.match(pattern,url):
        url1 = 'https://'+url+'/'
        html = requests.get(url1).text
        web = BeautifulSoup(html,'lxml')
        all_links = web.find_all('a')
        links = []
        for link in all_links:
            links.append(link.get('href'))
        return render(request,'siteapp/output.xml',{'url':links})
    else:
        return HttpResponse("Enter correctURL")
