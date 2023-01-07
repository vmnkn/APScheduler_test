from django.shortcuts import render


def test_aps(request, *args, **kwargs):
    return render(request, 'main.html', {})
