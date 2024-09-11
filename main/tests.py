from django.test import TestCase, Client
from .models import SurvivalEntry

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    # def test_survival_tool(self):
    #     tool = SurvivalEntry.objects.create(
    #       name = "Golok"
    #       price = 65000
    #       description = "Survival tool by Alatas"
    #     )
    #     //self.assertTrue(tool.is_mood_strong)