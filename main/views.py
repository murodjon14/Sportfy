from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class QoshiqchilarAPIView(APIView):
    def get(self, request):
        qoshiqchilar = Qoshiqchi.objects.all()
        serializers = QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response(serializers.data, status=201)

class QoshiqchiDeleteAPIView(APIView):
    def post(self, request):
        serializer = QoshiqchiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class QoshiqchiUpdatingAPIView(APIView):
    def put(self, requset, pk):
        qoshiqchi = get_object_or_404(Qoshiqchi, id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        qoshiqchi.delete()
        return Response(serializer.errors, status=400)

class AlbomlarModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

class QoshiqchilarModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer

    @action(detail=True, methods=['get'])
    def qoshiqchini_albomlari(self, request, pk):
        albom = self.get.object()
        qoshiqchi_albomlar = QoshiqchiAlbomlari.objects.filter()
        qoshiqchilar = Qoshiqchi.objects.filter()
        serializer = Qoshiqchi_AlbomlariSerializer(qoshiqchilar, many=True)
        return Response(serializer.data, status=200)

class AlbomlarModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomQoshiqSerializer

    @action(detail=True, methods=['get'])
    def albomni_qoshiqlari(self, request, pk):
        qoshiq = self.get.object()
        albomni_qoshiqlari = AlbomlarniQoashiqlari.objects.filter()
        albom = Albom.objects.filter()
        serializer = AlbomSerializer(qoshiq, many=True)
        return Response(serializer.data, status=200)

class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer


class AlbomQoshishModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

    @action(detail=True, methods=['post'])
    def albom_qoshish(self, request, pk):
        albom = self.get_object()
        serializer = AlbomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

