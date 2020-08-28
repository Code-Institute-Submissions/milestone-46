
from django import forms
from .models import Antiquity, Category


class AntiquityForm(forms.ModelForm):

    class Meta:
        model = Antiquity
        fields = (
            'category',
            'name',
            'date',
            'period',
            'culture',
            'dimensions',
            'description',
            'value',
            'image',
            'image2',
            'image3',
            'image4',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
