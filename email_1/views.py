# Task 3
import re
from django.http import HttpResponse


def verification(request):
    pattern = re.compile(r'^(?!.*--)(?!-)[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]@gmail\.com$')
    email_2 = input("Please enter your email address: ")
    matches = pattern.findall(email_2)

    if len(matches) > 0:
        return HttpResponse("your email address is correct :)")
    else:
        return HttpResponse("no correct email")