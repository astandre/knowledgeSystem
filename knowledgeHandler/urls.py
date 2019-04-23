from django.urls import path
from knowledgeHandler import views

urlpatterns = [
    path(r'knowledge', views.knowledge, name='knowledge'),
    path(r'api/knowledge/<int:id>', views.knowledge_api, name='knowledge_api'),

]
