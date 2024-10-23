from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics

# ====== estudante ======
class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

# ====== curso ======
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# ====== matricula ======
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


# ====== matricula/estudante ======
class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

# ====== matricula/curso ======
class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer

