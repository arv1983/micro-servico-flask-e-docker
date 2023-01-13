import json
import unittest
from flask import jsonify
import requests

class ApiTest(unittest.TestCase):
    URL_USER = "http://0.0.0.0:5000"
    URL_ORDER = "http://0.0.0.0:5002"

    USER_URL = "{}/user".format(URL_USER)
    GET_USER_CPF_URL = "{}/cpf".format(URL_USER)
    GET_ORDER_CPF_URL = "{}/order/cpf".format(URL_ORDER)

    OBJ_USER_CREATE = {
	    "name": "Nome Teste",
	    "cpf": "01555487009",
	    "email": "teste@teste.com",
	    "phone_number": "51985862273"
        }
    OBJ_USER_CREATE_INVALID_CPF = {
	    "name": "Nome Teste",
	    "cpf": "01555487001",
	    "email": "teste@teste.com",
	    "phone_number": "51985862273"
        }
    OBJ_CREATE_ORDER = {
        "user_id": 2,
        "item_description": "teste description",
        "item_quantity": 2,
        "item_price": 2.25
        }   
    

    

    def test_01_get_user(self):
        assert requests.get(ApiTest.URL_USER).status_code == 200

    def test_02_list_all_users_empty(self):
        assert requests.get(ApiTest.URL_USER).history == []
       
    def test_03_create_user(self):
        assert requests.post(ApiTest.URL_USER, json=ApiTest.OBJ_USER_CREATE).status_code == 201
        
    def test_04_recreate_user(self):
        assert requests.post(ApiTest.URL_USER, json=ApiTest.OBJ_USER_CREATE).status_code == 401
        
    def test_05_create_user_invalid_CPF(self):
        assert requests.post(ApiTest.URL_USER, json=ApiTest.OBJ_USER_CREATE_INVALID_CPF).status_code == 409
        
    def test_06_user_created_response(self):
        assert json.loads(requests.get(f'{ApiTest.GET_USER_CPF_URL}/{ApiTest.OBJ_USER_CREATE["cpf"]}').text)['cpf'] == "015.554.870-09"
        
    def test_07_user_edit(self):
        assert json.loads(requests.patch(f'{ApiTest.GET_USER_CPF_URL}/{ApiTest.OBJ_USER_CREATE["cpf"]}', json={'email': 'mynewemail@email.com'}).text)['email'] == "mynewemail@email.com"
        
    def test_08_delete_user(self):
        assert requests.delete(f'{ApiTest.GET_USER_CPF_URL}/{ApiTest.OBJ_USER_CREATE["cpf"]}').status_code == 200

    def test_08_delete_user(self):
        assert requests.delete(f'{ApiTest.GET_USER_CPF_URL}/{ApiTest.OBJ_USER_CREATE["cpf"]}').status_code == 200

    def test_09_recreate_user(self):
        assert requests.post(ApiTest.URL_USER, json=ApiTest.OBJ_USER_CREATE).status_code == 201    

    def test_10_create_order(self):
        assert requests.post(ApiTest.URL_ORDER, json=ApiTest.OBJ_CREATE_ORDER).status_code == 201    

    def test_11_get_order_by_cpf(self):
        assert json.loads(requests.get(f'{ApiTest.GET_USER_CPF_URL}/{ApiTest.OBJ_USER_CREATE["cpf"]}').text)['cpf'] == ApiTest.OBJ_USER_CREATE['cpf']

    def test_12_check_order_total_by_cpf_created(self):
        assert json.loads(requests.get(f'{ApiTest.GET_ORDER_CPF_URL}/{ApiTest.OBJ_USER_CREATE["cpf"]}').text)[0]['total_value'] == ApiTest.OBJ_CREATE_ORDER['item_quantity'] * ApiTest.OBJ_CREATE_ORDER["item_price"]


    

        


        

        



if __name__ == '__main__':
    unittest.main()        