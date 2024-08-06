# Task 2
import re
from django.http import HttpResponse


def validate_credit_card(request):
    card_number = input('Enter your card number: (Must be in format - 9999-9999-9999-9999): ')
    pattern = re.compile(r"^\d{4}-\d{4}-\d{4}-\d{4}$")

    if not pattern.match(card_number):
        return HttpResponse('<h4>Invalid card number<h4>')
    else:
        return HttpResponse('<h4>Your card number is valid<h4>')

