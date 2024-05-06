from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from drink.models import Drink
from drink.serializers import DrinkSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drink.forms import DrinkForm

# Create your views here.


@api_view(["POST"])
def num_square(request, val):
    if request.method == "POST":
        return_val = val * val
        return Response(return_val)


@api_view(["GET", "POST"])
def drink_list(request):
    if request.method == "GET":
        qs = Drink.objects.all()
        data = DrinkSerializer(qs, many=True).data
        return Response({"drinks": data})

    elif request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def drink_detail(request, id):
    print(f"request id is {id}")
    drink = get_object_or_404(Drink, id=id)

    if request.method == "GET":
        if drink:
            serializer = DrinkSerializer(drink).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT":
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def Index(request):
    drinks = Drink.objects.all()
    context = {
        "drinks": drinks
    }
    return render(request, "Drinks.html", context)


def Drink_detail(request, id):
    drink = get_object_or_404(Drink, id=id)

    context = {
        "drink": drink
    }

    return render(request, "Drink.html", context)


def Delete_drink(request, id):
    drink = get_object_or_404(Drink, id=id)
    context = {
        "drink": drink
    }
    if (request.method == "POST"):
        drink.delete()
        return redirect("/")
    return render(request, "del.html", context)


def update_drink(request, id):
    form = DrinkForm
    drink = get_object_or_404(Drink, id=id)

    if (request.method == "POST"):
        form = DrinkForm(request.POST, instance=drink)
        if (form.is_valid()):
            form.save()
            return redirect("/")
    else:
        form = DrinkForm(instance=drink)

    context = {"form": form}

    return render(request, "edit.html", context)


def create_drink(request):

    form = DrinkForm
    if request.method == "POST":
        form = DrinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "create.html", context)
