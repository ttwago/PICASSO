from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer
from .tasks import process_file

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

@action(detail=False, methods=['POST'])
def upload(self, request):
    uploaded_file = request.data.get('file')
    if not uploaded_file:
        return Response({'error': 'No file uploaded'}, status=status.HTTP_BAD_REQUEST)

    file_instance = File.objects.create(file=uploaded_file)
    process_file.delay(file_instance.id)
    serializer = FileSerializer(file_instance)

    return Response(serializer.data, status=status.HTTP_201_CREATED)