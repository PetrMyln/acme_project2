from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Birthday, Congratulation

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}
class BirthdayForm(forms.ModelForm):

    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        """
        fields = ('first_name', 'birthday') — вформе будут показаны толькоперечисленные полямодели;
        exclude = ('last_name',) — вформебудут показаны все полямодели, за исключением перечисленных;
        """
        exclude = ('author',)
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам
        # и возвращаем только первое имя.
        return first_name.split()[0]

    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if f'{first_name} {last_name}' in BEATLES:
            # Отправляем письмо, если кто-то представляется
            # именем одного из участников Beatles.
            send_mail(
                subject='Another Beatles member',
                message=f'{first_name} {last_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )


class CongratulationForm(forms.ModelForm):
    class Meta:
        model = Congratulation
        fields = ('text',)