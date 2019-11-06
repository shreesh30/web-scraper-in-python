from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from bs4 import BeautifulSoup
import json
from django.core import serializers
# Create your views here.

def prices(request):

    url="https://www.myprotein.co.in"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html5lib')
    protein_prices=[]
    final_protein={}
    root_div=soup.find('div',attrs={'id':'mainContent'})
    for item in root_div.findAll('div',attrs={'class':'sectionPeek_item'}):
        protein={}
        
        # for b in item.descendants:
            
            # name=b.get('class','athenaProductBlock_productName')
        span=item.find('span',attrs={'class':'js-enhanced-ecommerce-data athenaProductBlock_hiddenElement'})
        name=span.get('data-product-title')
        product_price=span.get('data-product-price')
        imageURL=item.find('img',attrs={'class':'athenaProductBlock_image'})
        image=imageURL.get('src')
        # print(name)
        protein['product_name']=name
        protein['price']=product_price[1:]
        protein['image']=image
        protein_prices.append(protein)
    final_protein['data']=protein_prices
    print(*final_protein)

    # protein_priceSerialized=serializers.serialize('json',protein_prices.all())
    # final_protein_prices=json.dumps(protein_prices)

    # print(final_protein_prices)

    return JsonResponse(final_protein,safe=False)


