from django.db import transaction

from rest_framework import status, generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import FileSerializer
from .tasks import task_execute


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            instance = serializer.save()
            instance_id = instance.id

            job_params = {"db_id": instance.id}

            transaction.on_commit(lambda: task_execute.delay(job_params))

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class AllFilesAPIView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
