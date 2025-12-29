from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # vuelve al dashboard
    else:
        form = ReservaForm()

    return render(request, 'reserva/crear_reserva.html', {'form': form})
