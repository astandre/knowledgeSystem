from .models import *


def get_subject_as_json(subject):
    triple = {}
    print("S>", subject)
    predicates = Predicate.objects.filter(subject=subject)
    for predicate_iter in predicates:
        if predicate_iter.property is not None:
            key_name = "%s:%s" % (predicate_iter.property.context.prefix, predicate_iter.property.property)
        else:
            key_name = predicate_iter.get_keyword_display()
        print("     P>", key_name)
        triple_object = Object.objects.get(predicate=predicate_iter)
        if triple_object.label is not None:
            print("         O>", triple_object.label)
            triple.update({key_name: triple_object.label})
        else:
            print("         O>", triple_object.object.__str__())
            new_triple = get_subject_as_json(triple_object.object)
            triple.update({key_name: new_triple})
    return triple


def clean_uri(uri):
    if uri.find('#') != -1:
        special_char = '#'
    else:
        special_char = '/'
    index = uri.rfind(special_char)
    return uri[index + 1:len(uri)]
