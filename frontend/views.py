from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def tech(request):
    return render(request, 'frontend/index.html')


@login_required
def cloth(request):
    return render(request, 'frontend/Cloth.html')


@login_required
def home(request):
    return render(request, 'frontend/Home.html')


@login_required
def profile(request):
    return render(request, 'frontend/profile.html')

@login_required
def offer_info(request, id):
    return render(request, 'frontend/offer_info.html', {"offer_id": id})
