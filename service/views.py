from django.shortcuts import render
from .models import Service, Order
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import CreateOrderForm, SendReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
# Create your views here.
def index(request):

    services = Service.objects.all()

    context = {
        'services': services
    }

    return render(request, 'service/services.html', context)


class CreateOrderView(CreateView, LoginRequiredMixin):
    template_name = 'service/create-order.html'
    form_class = CreateOrderForm
    success_url = '/my-orders/'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class MyOrdersListView(ListView):

    model = Order
    template_name = 'service/my-orders.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        orders = Order.objects.order_by('-order_date')

        return {
            'orders': orders
        }


class OrderDetailView(FormMixin, DetailView, LoginRequiredMixin):

    model = Order
    template_name = 'service/order_detail.html'
    context_object_name = 'order'
    form_class = SendReviewForm
    success_url = '/my-orders/'

    def post(self, req, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.order = self.get_object() #сохранение order'a
        self.object.client = self.request.user #сохранение клиента, оптавившего
        self.object.save()
        return super().form_valid(form)