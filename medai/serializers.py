from rest_framework import serializers
from .models import Metadata, Subject

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ['id', 'subject_id', 'study_uid', 'series_uid', 'image_uid']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject_id', 'research_group', 'sex', 'apoe', 'visit_identifier']