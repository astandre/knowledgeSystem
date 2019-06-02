from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import *
from rdflib import Graph, plugin, URIRef, RDF
from decouple import config
from .serializers import WordSerializer
from .services import *

# Create your views here.

if config('MAIN', cast=bool):
    local_url = config('MAIN_URL')
else:
    local_url = config('SLAVE_URL')


def knowledge(request):
    """
    View knowledge JSON
    """
    template = loader.get_template('knowledge.html')
    context = {
        "url": local_url
    }
    return HttpResponse(template.render(context, request))


def answer(request, word):
    template = loader.get_template('result.html')
    properties = []
    context = {}
    results = search(word)
    # print(results)
    if len(results) > 0:
        for result in results:
            # print(result)
            keys = list(result.keys())
            key = clean_uri(keys[1])
            value = clean_uri(result[keys[0]])
            # print(keys)
            data = {
                "key": key,
                "value": value
            }
            properties.append(data)
        context["word"] = word
        context["url"] = local_url
        context["properties"] = properties
        print('Going to result')
        print(context)
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
