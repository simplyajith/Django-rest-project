from django.test import TestCase
from rest_framework.test import APIClient

class AnimalTestCase(TestCase):
    client = APIClient()
    def test_post(self):
        data = {
            "firstname": "advik sxf",
            "lastname": "a",
            "emp_id": 9
            }
        response = self.client.post("/employees/",data=data)
        # print(response.content)
        assert response.status_code == 201

    def test_xet(self):
        response = self.client.get("/employees/")
        print(response.content)
        assert response.status_code == 200

    # def test_get_detail(self):
    #     response = self.client.get("/employees/1/")
    #     print(response.content)
    #     assert response.status_code == 200