from django.db import models

class Metadata(models.Model):
    subject_id = models.CharField(max_length=50)
    study_uid = models.CharField(max_length=50)
    series_uid = models.CharField(max_length=50)
    image_uid = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject_id} - {self.image_uid}"
    
    def get_related_visits(self):
        '''
        Retrun the different study visits the subject was present for.
        '''
        return Subject.visit_identifier(subject_id=self.subject_id)
    

   
    
class Subject(models.Model):
    # A db to subject details for a particular visit
    subject_id = models.CharField(max_length=50)
    research_group = models.CharField(max_length=5, blank=False)
    sex = models.CharField(max_length=5, blank=False)
    apoe = models.JSONField()
    visit_identifier = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return f"{self.subject_id} - {self.visit_identifier}"