from django.urls import path
from drink.views import *
urlpatterns = [
    path("", Index, name="Drinks"),
    path("drink/<int:id>/", Drink_detail, name="drink_detail"),
    path("drink/delete/<int:id>/", Delete_drink, name="drink_delete"),
    path("drink/edit/<int:id>/", update_drink, name="drink_update"),
    path("create", create_drink, name="create_drink"),


]
