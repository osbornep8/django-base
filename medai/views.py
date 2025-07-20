from django.http import HttpResponse
from django.shortcuts import render


# procees JSON variables with leading underscores within the view itself and store it to be called elsewhere
metadata_1 = { "metadata_1":{
  "_id": {
    "$oid": "67c95e5c5cfd98ba96e179cb"
  },
  "subject_id": "002_S_0295",
  "study_uid": "3566",
  "series_uid": "S13402",
  "image_uid": "I13712"
}}

def metadata(request):
    return render(request, "metadata/metadata.html", metadata_1)

def project_info(request):
    return HttpResponse("ADNI Project")