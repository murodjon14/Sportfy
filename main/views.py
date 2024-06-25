from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter


class QoshiqchilarAPIView(APIView):
    def get(self, request):
        qoshiqchilar = Qoshiqchi.objects.all()
        ism_search = request.query_params.get('ism', None)
        davlat_search = request.query_params.get('davlat', None)
        t_sana_search = request.query_params.get('t_sana', None)

        if ism_search is not None:
            qoshiqchilar = qoshiqchilar.filter(ism=ism_search)

        if davlat_search is not None:
            qoshiqchilar = qoshiqchilar.filter(davlat=davlat_search)

        if t_sana_search is not None:
            qoshiqchilar = qoshiqchilar.order_by(sana=t_sana_search)

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


class QoshiqAPIView(APIView):
    def get(self, request):
        qoshiq = Qoshiq.objects.all()
        nom_search = request.query_params.get('nom', None)
        janr_serach = request.query_params.get('janr', None)

        if nom_search is not None:
            qoshiq = qoshiq.filter(nom=nom_search)

        if janr_serach is not None:
            qoshiq = qoshiq.filter(janr=janr_serach)

        serializer = QoshiqSerializer(qoshiq, many=True)
        return Response(serializer.data, status=201)

class AlbomlarAPIView(APIView):
    def get(self, request):
        albom = Albom.objects.all()
        nom_search = request.query_params.get('nom', None)


        if nom_search is not None:
            albom = albom.filter(nom=nom_search)


        serializers = AlbomSerializer(albom, many=True)
        return Response(serializers.data, status=201)



class AlbomlarModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    order_fields = ['sana']

class QoshiqchilarModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    order_fields = ['t_sana']

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

    filter_backends = [SearchFilter, OrderingFilter]
    order_fields = ['davomiylik']


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

