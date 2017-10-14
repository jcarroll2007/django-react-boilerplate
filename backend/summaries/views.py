import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from django.http import HttpResponse

from summaries.serializers import DailySummarySerializer
from summaries.models import DailySummary


class DailySummaryModelViewSet(viewsets.ModelViewSet):
    serializer_class = DailySummarySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('date',)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the daily summaries
        for the currently authenticated user.
        """
        user = self.request.user
        return DailySummary.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        data = {}
        data["user"] = request.user
        data["date"] = request.data["date"]
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
