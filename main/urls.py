from django.urls import path
from . import views
from main.views import show_main, create_survival_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('create-survival-entry', create_survival_entry, name='create_survival_entry'),
    # path('entries/', views.survival_entry_list, name='survival_entry_list'),
    # path('add-to-cart/<int:entry_id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', views.view_cart, name='cart'),

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]