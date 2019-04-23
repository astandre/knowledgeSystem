# Knowledge System
1. Crear super usuario

`
python manage.py createsuperuser
`

2. Cargar data 

`
python manage.py loaddata initial_data
`

3. Lanzar servidor

`
python manage.py runserver
`

4. Acceder a la url http://127.0.0.1:8000/knowledge


##NOTA

En caso de necesitar exportar la base de datos usar el siguiente comando

`
dumpdata knowledgeHandler.context knowledgeHandler.key knowledgeHandler.subject knowledgeHandler.predicate knowledgeHandler.object
`