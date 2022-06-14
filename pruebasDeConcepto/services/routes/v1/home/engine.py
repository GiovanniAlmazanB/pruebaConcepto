import json
from numpy import average, maximum, product
import requests
from google.cloud import bigquery
from utilities.bigquery import priceIndex, otherPromos, productPromos, bigQuery

BigQuery_Client = bigquery.Client()

def graficasPrice():
        lista = []
        response = priceIndex()
        print(response)
        minimum = min(response)
        maximum = max(response)
        sum = sum(response)
        length = len(response)
        average = sum/length
        
       
        response = {
                    "cols": [
                    {"id":"","label":"Price by day of the week","pattern":"","type":"string"},
                    {"id":"","label":"Max Price","pattern":"","type":"number"},
                    {"id":"","label":"Medium Price","pattern":"","type":"number"},
                    {"id":"","label":"Minimun Price","pattern":"","type":"number"}
                    ],
                "rows": [
                    {"c":[{"v":"Monday","f":""},{"v":minimum,"f":""}, {"v":maximum,"f":""}, {"v":average,"f":""}]},
                ]
                }
            
        lista.append(list(response))
        response = json.dumps(list)
        print(response)
        return response
    
def graficaOtherPromo(body):
    if body!=None:
        response = otherPromos()
        for item in response:
            year_week = item['year_week']
            product_name = item['product_name']
            price_index = item['price_index']
            response={
                    
            }
    else:
            response = {
                "response: No se encontraron parametros"
            }
    return response
    
def graficaProductPromo(body):
    if body!=None:
        response = productPromos()
        for item in response:
            year_week = item['year_week']
            product_name = item['product_name']
            price_index = item['price_index']
            response={
                    
                }
    else:
        response = {
                "response: No se encontraron parametros"
            }
    return response

def priceDayOfWeek():
    lista = []
    response ={
        "cols": [
        {"id":"","label":"Price by day of the week","pattern":"","type":"string"},
        {"id":"","label":"Max Price","pattern":"","type":"number"},
        {"id":"","label":"Medium Price","pattern":"","type":"number"},
        {"id":"","label":"Minimun Price","pattern":"","type":"number"}
        ],
    "rows": [
        {"c":[{"v":"Monday","f":""},{"v":7192.00,"f":""}, {"v":69.00,"f":""}, {"v":9.90,"f":""}]},
        {"c":[{"v":"Tuesday","f":""},{"v":7192.00,"f":""}, {"v":69.00,"f":""}, {"v":9.90,"f":""}]},
        {"c":[{"v":"Wednesday","f":""},{"v":7192.00,"f":""}, {"v":69.00,"f":""}, {"v":69.00,"f":""}]},
        {"c":[{"v":"Thursday","f":""},{"v":7192.00,"f":""},{"v":69.00,"f":""}, {"v":8.01,"f":""}]},
        {"c":[{"v":"Friday","f":""},{"v":7192.00,"f":""}, {"v":69.00,"f":""}, {"v":3,"f":""}]},
        {"c":[{"v":"Saturday","f":""},{"v":7192.00,"f":""},{"v":69.00,"f":""},{"v":3,"f":""}]},
        {"c":[{"v":"Sunday","f":""},{"v":7192.00,"f":""},{"v":69.00,"f":""},{"v":3,"f":""}]}
      ]
    }
    lista.append(response)
    lista = json.dumps(lista)
    
    return response

def otherPromos():
    lista = []
    response ={
        "cols": [
        {"id":"","label":"Topping","pattern":"","type":"string"},
        {"id":"","label":"Slices","pattern":"","type":"number"}
      ],
  "rows": [
        {"c":[{"v":"Price Promos","f":"Price Promos"},{"v":17394.18,"f":""}]},
        {"c":[{"v":"Other Promos","f":"Other Promos"},{"v":148580.82,"f":""}]},
      ]
    }
    lista.append(response)
    lista = json.dumps(lista)
    
    return response

graficasPrice()