from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry
from django.db.models import Q


class EntriesList(LoginRequiredMixin,ListView):
    model = Entry
    template_name = 'entries/home.html'
    context_object_name = 'entries'
    paginate_by = 5


    def get_context_data(self, **kwargs):  # Overwrite method
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Home'
        return context
    
    def get_queryset(self): # Overwrite method
        return Entry.objects.filter(author = self.request.user).order_by('-date_posted')

class EntriesDetail(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'

    def get_context_data(self, **kwargs):  # Overwrite method
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Home'
        return context
    

class CreateEntry(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['title', 'content']
  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):  # Overwrite method
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Create Entry'
        return context

class DeleteEntry(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):  # Overwrite method
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Delete Entry'
        return context

class UpdateEntry(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ['title', 'content']

    def get_context_data(self, **kwargs):  # Overwrite method
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Edit Entry'
        return context

class SearchEntry(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'entries/search_results.html'
    context_object_name = 'entries'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('search_entries')
        if user:
            object_list = Entry.objects.filter(
                Q(title__icontains=query) | (Q(content__icontains=query))).filter(author=user)
        return object_list
    
    def get_context_data(self, **kwargs):  # Overwrite method
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Search Entries'
        return context