from django import forms
from .models import Sale
from inventory.models import Product

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer']

class ProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1)
    selling_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        selling_price = cleaned_data.get('selling_price')
        if product and selling_price and selling_price < product.buying_price:
            raise forms.ValidationError("Selling price cannot be less than buying price")
        if product and not selling_price:
            cleaned_data['selling_price'] = product.selling_price
        return cleaned_data
