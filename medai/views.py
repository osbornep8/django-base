from django.http import HttpResponse
from django.shortcuts import render


# procees JSON variables with leading underscores within the view itself and store it to be called elsewhere
data = { 
    "metadata":[
        {
  "subject_id": "002_S_0295",
  "study_uid": "3566",
  "series_uid": "S13402",
  "image_uid": "I13712",
}, 
{
  "subject_id": "002_S_0295",
  "study_uid": "3566",
  "series_uid": "S13402",
  "image_uid": "I13713",
},
{
  "subject_id": "002_S_0295",
  "study_uid": "5726",
  "series_uid": "S21853",
  "image_uid": "I28556",
},
]}

def metadata(request):
    return render(request, "metadata/metadata.html", data)

def project_info(request):
    return HttpResponse("ADNI Project")