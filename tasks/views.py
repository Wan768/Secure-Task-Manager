from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm
import logging

class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        
        status_filter = self.request.GET.get('status-filter')
        if status_filter and status_filter != 'All':
            queryset = queryset.filter(status=status_filter)
            
        return queryset.order_by(F('deadline').asc(nulls_last=True))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_filter'] = self.request.GET.get('status-filter', 'All')
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'

    # IDOR Prevention
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm  
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm 
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/task_form.html'

    # IDOR Prevention
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

logger = logging.getLogger('security')
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def form_valid(self, form):
        task = self.get_object()
        logger.warning(
            f"SECURITY AUDIT: User '{self.request.user.username}' deleted Task ID {task.id} (Title: '{task.title}')"
        )
        return super().form_valid(form)
