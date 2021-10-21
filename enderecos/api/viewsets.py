from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer


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

