from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Metadata


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
    data = Metadata.objects.all()
    return render(request, "metadata/metadata.html", {"metadata": data})

def project_info(request):
    return HttpResponse("ADNI Project")

def detail(request, id):
    data = Metadata.objects.get(pk=id)
    return render(request, "metadata/detail.html", {"patient": data})

def add(request):
    subject_id = request.POST.get("subject_id")
    study_uid = request.POST.get("study_uid")
    series_uid = request.POST.get("series_uid")
    image_uid = request.POST.get("image_uid")

    if subject_id and study_uid and series_uid and image_uid:
        metadata = Metadata(subject_id=subject_id, study_uid=study_uid, series_uid=series_uid, image_uid=image_uid)
        metadata.save()
        return HttpResponseRedirect('/metadata')
    return render(request, "metadata/add.html")
    
def delete(request, id):
  try:
     metadata = Metadata.objects.get(pk=id)
  except:
      raise Http404("Movie Does Not Exist!")
  metadata.delete()
  return HttpResponseRedirect("/metadata")