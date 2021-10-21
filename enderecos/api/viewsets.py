from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer

import pycep_correios
from pycep_correios.exceptions import CEPNotFound


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        cep = self.request.query_params.get('cep', None)
        queryset = Endereco.objects.all()

        if id:
            queryset = Endereco.objects.filter(pk=id)

        if cep:
            queryset = queryset.filter(cep=cep)

        return queryset

    def create(self, request, *args, **kwargs):

        try:
            endereco = pycep_correios.get_address_from_cep(request.data.get('cep'))
        except CEPNotFound as exc:
            return CEPNotFound('CEP não encontrado!')

        return super(EnderecoViewSet, self).create(request, *args, **kwargs)
