from rest_framework.fields import SlugField
from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco

from rest_framework.validators import UniqueValidator


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'CEP', 'linha1', 'linha2', 'cidade', 'estado',
            'pais', 'latitude', 'longitude', ]
