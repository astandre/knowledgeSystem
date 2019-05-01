from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import *
from rdflib import Graph, plugin, URIRef, RDF
from decouple import config
from .serializers import WordSerializer
from .services import *
import json
import types
import itertools


# Create your views here.


def knowledge(request):
    """
    View knowledge JSON
    """
    template = loader.get_template('knowledge.html')
    if config('MAIN', cast=bool):
        local_url = config('MAIN_URL')
    else:
        local_url = config('SLAVE_URL')
    context = {
        "url": local_url
    }
    return HttpResponse(template.render(context, request))


def answer(request, word):
    template = loader.get_template('result.html')
    keys = []
    values = []
    keys_clean = []
    values_clean = []
    properties = []
    context = {}
    result = search(word)
    print(result)
    if len(result) > 0:
        for i in result:
            for j in i.keys():
                keys.append(j)
            for k in i.values():
                values.append(k)
        for i in keys:
            if i == "@id":
                keys_clean.append(i)
            else:
                str = i
                str1 = str.rsplit('/', 1)[1]
                keys_clean.append(str1)

        for i in values:
            if type(i) is list:
                str = i[0].get("@id")
                str = str.rsplit('/', 1)[1]
                values_clean.append(str)
            else:
                str = i.rsplit('/', 1)[1]
                values_clean.append(str)

        for k, v in zip(keys_clean, values_clean):
            data = {
                "key": k,
                "value": v
            }
            # data[k] = v
            properties.append(data)
        context["properties"] = properties
    return HttpResponse(template.render(context, request))


@api_view(['GET'])
def knowledge_api(request):
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


@api_view(['POST'])
def read_rdf(request):
    if request.method == 'POST':
        word_serializer = WordSerializer(data=request.data)
        if word_serializer.is_valid():
            g = Graph()
            if config('MAIN', cast=bool):
                print("Using data 4")
                g.parse("data4.rdf")
            else:
                print("Using data 2")
                g.parse("data2.rdf")
            print("graph has %s statements." % len(g))
            link = "http://example.com/resources/" + word_serializer.data["word"]
            LE = URIRef(link)
            # Para que busque todos los datos relacionanados
            resultGraph = Graph()
            resultGraph += g.triples((None, None, LE))
            # for s, p, o in resultGraph :
            #    print("{0}  __________________   {1}\n".format(s, o))

            return HttpResponse(resultGraph.serialize(format='json-ld'), content_type="application/ld+json")
        else:
            return JsonResponse(word_serializer.errors, status=status.HTTP_404_NOT_FOUND)
