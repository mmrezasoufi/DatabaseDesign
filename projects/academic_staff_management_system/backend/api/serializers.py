class ResearcherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Researcher
        fields = "__all__"


class ResearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Research
        fields = "__all__"


class ResearchMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ResearchMember
        fields = "__all__"


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Schedule
        fields = "__all__"


class LaboratorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Laboratory
        fields = "__all__"


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Library
        fields = "__all__"