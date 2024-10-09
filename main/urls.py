from django.urls import path
from . import views
from main.views import show_main, create_survival_entry, edit_survival_entry, delete_survival_entry, add_survival_entry_ajax    
from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('create-survival-entry', create_survival_entry, name='create_survival_entry'),
    path('edit-mood/<uuid:id>', edit_survival_entry, name='edit_survival_entry'),   
    path('delete/<uuid:id>', delete_survival_entry, name='delete_survival_entry'),
    path('create-survival-entry-ajax', add_survival_entry_ajax, name='add_survival_entry_ajax'),
 

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]