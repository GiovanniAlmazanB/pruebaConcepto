from http import HTTPStatus
from urllib import response
from flask import Blueprint
from flask import request, render_template

# local library
from configuration.setup import headers
from services.routes.v1.home.engine import graficaProductPromo, graficaOtherPromo, otherPromotion,priceDayOfWeek
from utilities.bigquery import otherPromos

# [global variables]
v1 = Blueprint("version1", "version1", url_prefix="/v1")


# [consulta cliente baz]
@v1.route('/priceDayWeek', methods=['GET','OPTIONS'])
def priceWeek():
    if request.method == 'OPTIONS':
        return ('', HTTPStatus.NO_CONTENT,headers)

    if request.method == 'GET':
        response = priceDayOfWeek()
        return (response,headers)
    
@v1.route('/pricePromo', methods=['GET','OPTIONS'])
def promoPrice():
    if request.method == 'OPTIONS':
        return ('', HTTPStatus.NO_CONTENT,headers)

    if request.method == 'GET':
        response = otherPromotion()
        return (response,headers)

