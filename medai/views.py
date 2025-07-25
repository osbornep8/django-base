from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from .serializers import MetadataSerializer, SubjectSerializer, SubjectIDSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Metadata, Subject


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
{
    "subject_id": "002_S_0295", 
    "research_group": "CN",
    "sex": "M",
    "apoe": {"APOE_A1": 3, "APOE_A2": 4},
    "visit_identifier": "ADNI1/GO Month 6"
}
]}

# @api_view('GET')
def metadata(request):

    # if request.methods == GET:
    data = Metadata.objects.all()
    metadata_serializer = MetadataSerializer(data, many=True)
    return render(request, "metadata/metadata.html", {"metadata": metadata_serializer.data})
    
        # This just gives the JSON response and if you add `{"metadata": metadata_serializer.data}` in the JSONResponse() it returns it as an object which is what I assume happens a
        # return JsonResponse(metadata_serializer.data, safe=False)
    

@api_view(http_method_names=['GET', 'POST'])
def subject_info(request):

    # if request.method == 'GET':
    #     data = Subject.objects.all()
    #     sub_serializer = SubjectSerializer(data, many=True)
    #     return JsonResponse(sub_serializer.data, safe=False)

    if request.method == "GET":
        subject_id = Subject.objects.all()
        serializer = SubjectIDSerializer(subject_id, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid(): serializer.save()
        # This is the preferred way than JsonResponse as it is part of the rest_framework
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def project_info(request):
    return HttpResponse("ADNI Project")


def meta_detail(request, id):
    data = Metadata.objects.get(pk=id)
    return render(request, "metadata/detail.html", {"patient": data})

@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail(request, id):

    try:
        subject = Subject.objects.get(pk=id)
    except Subject.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

def home(request):
    return render(request, "homepage/home.html")