# Task 1
import re
from django.http import HttpResponse


def reg_expr(request):
    text = "abab, Rbbbr, dsbrasd, rbbbr, rbr, ffk, rBbr"
    pattern = re.compile(r'(?i)Rb+r')
    matches = pattern.findall(text)

    if len(matches) > 0:
        return HttpResponse({f"correct: {matches}"})
    else:
        return None
