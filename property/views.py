from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Property
from django.views.generic.edit import FormMixin
from .forms import PropertyBookForm, PropertyForm
from .filter import PropertyFilter
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class PropertyList(FilterView):
    model = Property
    paginate_by = 3
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'

    # template_name = 'property/property_list.html'
    # context_object_name = 'properties'

class PropertyDetail(FormMixin,DetailView):
    model = Property
    form_class = PropertyBookForm
    # template_name = 'property/property_detail.html'
    # context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Property.objects.filter(category=self.get_object().category)[:2]
        return context
    
    def post(self,request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()    
            return redirect('/')
        
        else:
            print('not valid')
            
            
# class AddListing(CreateView):
#     model = Property
#     # template_name = 'property/add_listing.html'
#     # fields = ['title','description','price','location','category','image']
#     # success_url = '/property/listing'
#     # def form_valid(self,form):
#     #     form.instance.user = self.request.user
#     #     return super().form_valid(form)
#     # def form_invalid(self,form):
        
               
class PropertyCreate(LoginRequiredMixin, CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'property/property_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
            
            
            
            
            

class PropertyUpdate(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'property/property_update.html'
    context_object_name = 'property'

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)


class PropertyDelete(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = 'property/property_confirm_delete.html'
    success_url = reverse_lazy('accounts:mylisting')
    context_object_name = 'property'

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)
