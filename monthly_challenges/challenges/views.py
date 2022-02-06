from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    "january": "Learn Django",
    "february": "Learn French",
    "march": "Learn Django",
    "april": "Learn French",
    "may": "Learn Django",
    "june": "Learn French",
    "july": "Learn Django",
    "august": "Learn French",
    "september": "Learn Django",
    "october": "Learn French",
    "november": "Learn Django",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month-1]
    redirect_path = reverse(
        'month-challenge', args=[redirect_month])  # challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        raise Http404()