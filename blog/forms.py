from django import forms
from blog.models import upload

class Myfile(forms.ModelForm):
    class Meta:
        model=upload
        fields="__all__"
    def __init__(self, *args, **kwargs):
                super(Myfile, self).__init__(*args, **kwargs)
                for field_name, field in self.fields.items():
                    field.widget.attrs['class'] = 'form-control'         
