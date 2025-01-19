from django import forms
from .models import Product, TypeProduct


class ProductForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=TypeProduct.objects.all(), label="Тип товара")

    class Meta:
        model = Product
        fields = ['name', 'type', 'description', 'price', 'count_storage', 'image']
        widgets = {
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': 'any'
            }),
            'count_storage': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': 'any'
            }),
            'count_sells': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': 'any'
            }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

    def clean_count_storage(self):
        count_storage = self.cleaned_data.get('count_storage')
        if count_storage is not None and count_storage < 0:
            raise forms.ValidationError("Количество на складе не может быть отрицательным.")
        return count_storage


class TypeProductForm(forms.ModelForm):
    class Meta:
        model = TypeProduct
        fields = ['name', 'description', 'image']


class EditTypeProductForm(TypeProductForm):
    pass
