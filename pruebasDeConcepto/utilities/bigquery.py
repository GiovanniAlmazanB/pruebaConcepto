#google library
from urllib import response
from google.cloud import bigquery

#Standar library
import requests
import json
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C://Users/USER/Documents/keysAtlantia/ecomm-mx-jla054-modelorama-860e84ba1458.json"

def priceIndex():
    client=bigquery.Client()
    response = []
    min = client.query("""
        SELECT min(product_current_price) FROM `ecomm-mx-jla054-modelorama.views_bi.vw_product_prices` 
            """)
    min = min.result()
    maxi = client.query("""
        SELECT max(product_current_price) FROM `ecomm-mx-jla054-modelorama.views_bi.vw_product_prices` 
            """)
    maxi = maxi.result()
    avg = client.query("""
        SELECT avg(product_current_price) FROM `ecomm-mx-jla054-modelorama.views_bi.vw_product_prices` 
            """)
    avg = avg.result()
    
    print(response, maxi, min, avg)
    return response, maxi, min, avg

def otherPromos():
    client=bigquery.Client()
    response = []
    query_job = client.query(f"""
        SELECT 
            master_date_id,
            retailer_id,
            store_id,
            master_product_id,
            num_other_promos
        FROM (
            SELECT 
                master_date_id, 
                retailer_id, 
                store_id, 
                master_product_id, 
                ARRAY_LENGTH(dwh.product_promotion_list) AS num_other_promos
                -- other_promotion
            FROM `views_bi.mv_ecommerce_products` AS dwh

        ) AS tbl_other_promos
        WHERE num_other_promos > 0 and retailer_id == {retailer}
        
            """)
    results=query_job.result()
    for i in results: 
        response.append(i)
    return response

def bigQuery():
    BigQuery_Client = bigquery.Client()
    response = """

    SELECT * FROM `ecomm-mx-jla054-modelorama.ecommerce_data.price_index` 
            """
    return response

def productPromos():
    client=bigquery.Client()
    response = []
    query_job=client.query("""
        SELECT master_date_id,
            retailer_id,
            store_id,
            master_product_id,
            product_promo_price
        FROM `views_bi.mv_ecommerce_products`
        WHERE product_promo_price > 0
        
            """)
    results=query_job.result()
    for i in results: 
        response.append(i)
    print(response)
    return response

priceIndex()