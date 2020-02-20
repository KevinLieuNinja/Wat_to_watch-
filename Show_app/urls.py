from django.urls import path
from . import views

urlpatterns= [
    path('', views.index),
    path('view_show/<int:id>', views.view_show),
    path('edit_show/<int:id>',views.edit_show),
    path('add_show',views.add_show),
    path('create_show',views.create_show),
    path('delete_show/<int:id>',views.delete_show),
    path('update_show/<int:id>', views.update_show),
]