from django.forms import ModelForm
from page.models import Codigo
from django.contrib.auth.models import User

class CodigoForm(ModelForm):
    class Meta:
        model = Codigo
        exclude = ['codigo', 'promedio11', 'promedio2', 'promedio21', 'promedio22', 'promedio3', 'promedio31', 'promedio32', 'promedio4', 'promedio41', 'promedio42', 'promedio43', 'promedio5', 'promedio51', 'promedio52', 'promedio6', 'promedio61', 'promedio62', 'promedio63', 'promedio64', 'promedio65', 'promedio66', 'promedio67', 'promedio68', 'promedio69', 'promedio610', 'promedio7', 'promedio71', 'promedio72', 'promedio73', 'promedio74', 'promedio75', 'promedio76', 'promedio77', 'promedio8', 'promedio81', 'promedio82', 'promedio83', 'promedio84', 'promedio85', 'promedio86', 'promedio9', 'promedio91', 'promedio92', 'promedio10', 'promedio101', 'promedio011', 'promedio111', 'promedio112', 'promedio113']

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'last_name', 'id']
