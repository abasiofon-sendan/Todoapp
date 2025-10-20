from django.urls import path
from .views import FruitStorageView,UpdateFruitView

urlpatterns=[
    path('fruitstorage',FruitStorageView.as_view(),name='fruit'),
    path('update-fruit/<int:id>',UpdateFruitView.as_view(),name='fruit')
    
]