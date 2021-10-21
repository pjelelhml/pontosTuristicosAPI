from rest_framework.fields import SlugField
from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco

from rest_framework.validators import UniqueValidator


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'linha1', 'linha2', 'cidade', 'estado', 'pais',
            'latitude', 'longitude']

    slug = SlugField(
        max_length=100,
        validators=[UniqueValidator(queryset=Endereco.objects.all())]
    )