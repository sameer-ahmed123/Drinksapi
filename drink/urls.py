from django.urls import path
from drink.views import *
urlpatterns = [
    path("", drink_list),
    path('drink/<int:id>', drink_detail),
    path("sqr/<int:val>",num_square),
]
 