from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Sale
from .forms import SaleForm, ProductForm

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

def create_sale(request):
    ProductFormSet = formset_factory(ProductForm, extra=1)
    if request.method == 'POST':
        sale_form = SaleForm(request.POST)
        formset = ProductFormSet(request.POST)
        if sale_form.is_valid() and formset.is_valid():
            sale = sale_form.save()
            grand_total_price = 0
            for form in formset:
                product = form.cleaned_data['product']
                quantity = form.cleaned_data['quantity']
                selling_price = form.cleaned_data['selling_price']
                total_price = quantity * selling_price
                grand_total_price += total_price
                # Save product details to the sale (you can customize this part)
            sale.grand_total_price = grand_total_price
            sale.save()
            return redirect('sale_detail', pk=sale.pk)
    else:
        sale_form = SaleForm()
        formset = ProductFormSet()
    return render(request, 'sales/create_sale.html', {'sale_form': sale_form, 'formset': formset})