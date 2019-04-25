from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .utils import *
from rdflib import Graph,plugin
import pprint
from rdflib.serializer import Serializer
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
def knowledge_api(request, id):
    """
    End point where knowledge data comes
    :param request:
    :return:
    """
    if request.method == 'GET':
        resp = {}
        subject = Subject.objects.get(id=id)
        context = {}
        contexts = Context.objects.all()
        for context_iter in contexts:
            context.update(
                {context_iter.prefix: context_iter.url})
        resp.update({"@context": context})
        resp.update(get_subject_as_json(subject))
        print(resp)
        return JsonResponse(resp, status=status.HTTP_200_OK)

# TODO  crear arreglos cuando exista la misma propiedad
#       Presentar el nombre del objeto sino tiene valores


@api_view(['GET'])
def read_rdf(request):
    g = Graph()
    g.parse("data4.rdf")
    print("graph has %s statements." % len(g))
    for stmt in g:
        pprint.pprint(stmt)
    print(g.serialize(format='json-ld'))
    fuck = {"f": 1, "u": 2, "c": 4, "k": 4,"long":len(g)}
    return HttpResponse(g.serialize(format='json-ld'))