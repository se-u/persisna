from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy
import csv
import datetime
now = datetime.date.today()
from .forms import PresenceForm
from .models import Presence
# Create your views here.

class PresenceView(SuccessMessageMixin, CreateView):
    form_class = PresenceForm
    template_name = 'attendances/presence_form.html'
    success_url =  reverse_lazy('presence')
    success_message = "Anda Berhasil Absen"

class PresenceList(LoginRequiredMixin, ListView):
    model = Presence
    
class PresenceDetailView(DetailView):
    model = Presence

class SearchPresence(ListView):
    model = Presence
    template_name = 'attendances/presence_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  Presence.objects.filter(
            Q(name__icontains=query) | Q(classroom__icontains=query)
        )
        return object_list


@login_required
def export_presence(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="Daftar hadir persisna - {now}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Kelas', 'Tanggal'])

    presences = Presence.objects.all().values_list('name', 'classroom', 'date')
    for presence in presences:
        writer.writerow(presence)

    return response
