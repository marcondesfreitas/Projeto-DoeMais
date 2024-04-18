from rest_framework import serializers
from geral import models

class ProdutosSerializers(serializers.ModelSerializer):
    class Meta:
       model = models.Publicacao
       fields = '__all__'

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
       model = models.Usuario
       fields = '__all__'