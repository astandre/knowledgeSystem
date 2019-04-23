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

        resp = {
            "triples": []
        }
        subjects = Subject.objects.all()
        for subject in subjects:
            triple = {}
            print("S>", subject)
            triple.update({"@context": subject.context.url})
            predicates = Predicate.objects.filter(subject=subject)
            for predicate in predicates:
                # print("P>", predicate)
                print("     P>", predicate.property.property)
                triple_object = Object.objects.get(predicate=predicate)
                print("         O>", triple_object)
                if triple_object.label is not None:
                    triple.update({predicate.property.property: triple_object.label})
                else:
                    triple.update({predicate.property.property: triple_object.object.__str__()})
            print(triple)
            resp["triples"].append(triple)
        # response = {
        #     "triples": list(
        #         Subject.objects.values("context__url", "value", "predicate__property__property",
        #                                "predicate__object__label",
        #                                "predicate__object__object").all())
        # }

        return JsonResponse(resp, status=status.HTTP_200_OK)
