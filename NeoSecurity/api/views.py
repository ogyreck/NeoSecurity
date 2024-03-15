from rest_framework import viewsets, status
from rest_framework.decorators import api_view


from .permisions import IsModerator, IsStaff
from .serializers import GradeSerializer, GroupSerializer, \
    DocumentSerializer, DocumentCreateSerializer
from workers.models import Grade, Group, Document


class GradeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsModerator, ]
    pagination_class = None
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsModerator, ]
    pagination_class = None
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaff, IsModerator]
    pagination_class = None
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DocumentSerializer
        return DocumentCreateSerializer

