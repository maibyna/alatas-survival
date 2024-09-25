from django.forms import ModelForm
from main.models import SurvivalEntry

class SurvivalEntryForm(ModelForm):
    class Meta:
        model = SurvivalEntry
        fields = ["name", "price", "description"]

