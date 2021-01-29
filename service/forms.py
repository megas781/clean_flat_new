from django import forms
from .models import Order, Review
from django.forms import DateInput, ChoiceField

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateOrderForm(forms.ModelForm):

    class Meta:
        model = Order

        # my_date_field = forms.DateField(widget=DateInput(format='%d-%m-%Y',attrs={'class': 'form-control'}))
        # service_type = ChoiceField(choices=('supporting', 'full', 'after_renovation'), required=True),

        fields = ['service_type','room_count', 'bathroom_count', 'address', 'order_date']
        widgets = {
            'order_date': DateInput(format='%d.%m.%Y', attrs={
                'class': 'form-control'
            })
        }

class SendReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'scores']