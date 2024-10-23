from django.shortcuts import render


# eto yung gumagana na 
def home(request):
    return render(request, 'pos/pos.html')