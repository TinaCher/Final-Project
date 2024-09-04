import pytest
import allure
from api_page import ChitaiGorodApi

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjU2MzY5NzksImlhdCI6MTcyNTQ2ODk3OSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijk0MzZkNzcyMzE4NzY4M2Y0ZTAzNTMyMWZhNjk3NThlNThlZWI5YWMwODQ1MDkzMzBmMzQzNjljY2EzZDQwNjciLCJ0eXBlIjoxMH0.iewdI8wpg7Yazwv1jTTss3KEdvkLQNFHNl2AmzhGH9M"
api = ChitaiGorodApi('https://web-gate.chitai-gorod.ru/api/v1', token)

@allure.severity("Major")
@allure.id("T-1")
@allure.feature("Search")
@allure.title("Search by book name in russian")
def test_by_name_rus():
    name = "Рецепты"
    resp_search = api.by_name(name)
    assert resp_search.status_code == 200
    assert name in resp_search.text

@allure.severity("Major")
@allure.id("T-2")
@allure.feature("Search")
@allure.title("Search by book name in english")
def test_by_name_eng():
    name = "English"
    resp_search = api.by_name(name)
    assert resp_search.status_code == 200
    assert name in resp_search.text

@allure.severity("Major")
@allure.id("T-3")
@allure.feature("Search")
@allure.title("Search not existing name")
def test_not_existing():
    name = "mnsfdfhgogb"
    resp_search = api.by_name(name)
    assert resp_search.status_code == 200
    assert name not in resp_search.text

@allure.severity("Normal")
@allure.id("T-4")
@allure.feature("Add_cart")
@allure.title("Add book to cart")
def test_add_cart():
    id = "2676103"
    resp_add = api.add_cart()
    assert resp_add.status_code == 200
    resp_check_cart = api.check_cart()
    assert id in resp_check_cart.text

@allure.severity("Normal")
@allure.id("T-5")
@allure.feature("Clear_cart")
@allure.title("Delete book from cart")
def test_delete_cart():
    resp_delete = api.clear_cart()
    assert resp_delete.status_code == 204
   