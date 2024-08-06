# Task 4
from django.http import HttpResponse
import re


def login_verification(request):
    pattern = re.compile("^[a-zA-Z0-9]{2,10}$")
    login_2 = input("Please enter your password(login): ")

    matches = pattern.findall(login_2)

    if len(matches) > 0:
        return HttpResponse("your login is correct :)")
    else:
        return HttpResponse("no correct login")
