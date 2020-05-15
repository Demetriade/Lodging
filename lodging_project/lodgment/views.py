from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lodge


def home(request):
    context = {
        'lodges': Lodge.objects.all()
    }
    return render(request, 'lodgment/home.html', context)


class LodgeListView(ListView):
    model = Lodge
    template_name = 'lodgment/home.html'
    context_object_name = 'lodges'


class LodgeDetailView(DetailView):
    model = Lodge


class LodgeCreateView(LoginRequiredMixin, CreateView):
    model = Lodge
    fields = ['address', 'postal_code', 'image', 'total_nb', 'lodged_nb', 'information']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class LodgeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lodge
    fields = ['address', 'postal_code', 'image', 'total_nb', 'lodged_nb', 'information']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        lodge = self.get_object()
        if self.request.user == lodge.owner:
            return True
        return False


class LodgeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lodge
    success_url = '/'

    def test_func(self):
        lodge = self.get_object()
        if self.request.user == lodge.owner:
            return True
        return False