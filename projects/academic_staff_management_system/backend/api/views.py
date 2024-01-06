class ResearcherViewSet(viewsets.ModelViewSet):
    queryset = models.Researcher.objects.all()
    serializer_class = serializers.ResearcherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResearchViewSet(viewsets.ModelViewSet):
    queryset = models.Research.objects.all()
    serializer_class = serializers.ResearchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResearchMemberViewSet(viewsets.ModelViewSet):
    queryset = models.ResearchMember.objects.all()
    serializer_class = serializers.ResearchMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LaboratoryViewSet(viewsets.ModelViewSet):
    queryset = models.Laboratory.objects.all()
    serializer_class = serializers.LaboratorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = models.Library.objects.all()
    serializer_class = serializers.LibrarySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
