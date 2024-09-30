from django import forms
from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        """
        fields = ('first_name', 'birthday') — вформе будут показаны толькоперечисленные полямодели;
        exclude = ('last_name',) — вформебудут показаны все полямодели, за исключением перечисленных;
        """
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
