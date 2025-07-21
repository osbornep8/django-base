from django.db import models

class Metadata(models.Model):
    subject_id = models.CharField(max_length=50)
    study_uid = models.CharField(max_length=50)
    series_uid = models.CharField(max_length=50)
    image_uid = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject_id} - {self.image_uid}"