from django.urls import path
from knowledgeHandler import views

urlpatterns = [
    path(r'knowledge', views.knowledge, name='knowledge'),
    path(r'answer/<str:word>', views.answer, name='answer'),
    path(r'api/knowledge/<int:id>', views.knowledge_api, name='knowledge_api'),
    path(r'rdf', views.read_rdf, name='read_rdf'),
]
