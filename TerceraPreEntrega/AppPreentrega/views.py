from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from AppPreentrega.models import Barbero, Cliente, Servicio, Turno


#       ===== BARBEROS =====
class BarberoListView(ListView):
    model           = Barbero
    template_name   = 'lista_barberos.html'

class BarberoCreateView(CreateView):
    model = Barbero
    fields = ('nombre', 'apellido', 'dni', 'especialidad')
    success_url = reverse_lazy('lista_barberos')

class BarberoUpdateView(UpdateView):
    model = Barbero
    fields = ('nombre', 'apellido', 'dni', 'especialidad')
    success_url = reverse_lazy('lista_barberos')

class BarberoDetailView(DetailView):
    model = Barbero
    success_url = reverse_lazy('lista_barberos')

class BarberoDeleteView(DeleteView):
    model = Barbero
    success_url = reverse_lazy('lista_barberos')







#       ===== CLIENTES =====
class ClienteListView(ListView):
    model = Cliente
    template_name = 'lista_clientes.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ('nombre', 'apellido', 'dni', 'telefono', 'email')
    success_url = reverse_lazy('clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ('nombre', 'apellido', 'dni', 'telefono', 'email')
    success_url = reverse_lazy('clientes')

class ClienteDetailView(DetailView):
    model = Cliente
    success_url = reverse_lazy('clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')

def ClienteBuscarPorApellido(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        clientes = Cliente.objects.filter(apellido__contains=busqueda)
        contexto = {
            "object_list": clientes,
        }
        http_response = render(
            request=request,
            template_name='lista_clientes.html',
            context=contexto,
        )
        return http_response





#           ===== SERVICIOS =====

class ServicioListView(ListView):
    model = Servicio
    template_name = 'lista_servicios.html'

class ServicioCreateView(CreateView):
    model = Servicio
    fields = ('tipo', 'duracion_minutos', 'costo')
    success_url = reverse_lazy('servicios')

class ServicioUpdateView(UpdateView):
    model = Servicio
    fields = ('tipo', 'duracion_minutos', 'costo')
    success_url = reverse_lazy('servicios')

class ServicioDetailView(DetailView):
    model = Servicio
    success_url = reverse_lazy('servicios')

class ServicioDeleteView(DeleteView):
    model = Servicio
    success_url = reverse_lazy('servicios')




#           ===== TURNOS =====
class TurnoListView(ListView):
    model = Turno
    template_name = 'lista_turnos.html'

class TurnoCreateView(CreateView):
    model = Turno
    fields = ('cliente', 'barbero', 'servicio', 'fecha_turno', 'hora_turno')
    success_url = reverse_lazy('turnos')

class TurnoUpdateView(UpdateView):
    model = Turno
    fields = ('cliente', 'barbero', 'servicio', 'fecha_turno', 'hora_turno')
    success_url = reverse_lazy('turnos')

class TurnoDetailView(DetailView):
    model = Turno
    success_url = reverse_lazy('turnos')

class TurnoDeleteView(DeleteView):
    model = Turno
    success_url = reverse_lazy('turnos')



