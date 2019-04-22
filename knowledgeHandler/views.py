from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from django.db.models import F

# Create your views here.

def knowledge(request):
    """
    View knowledge JSON
    """
    template = loader.get_template('knowledge.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


@api_view(['GET'])
def knowledge_api(request):
    """
    End point where knowledge data comes
    :param request:
    :return:
    """
    if request.method == 'GET':
        response = {
            "triples": list(
                Subject.objects.values("context__url", "value", "predicate__property__property", "predicate__object__label",
                                       "predicate__object__object").all())
        }
        print(response)
        return JsonResponse(response, status=status.HTTP_200_OK)
