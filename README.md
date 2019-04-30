# Knowledge System

Crear dos carpetas del mismo proyecto, para  correr el proyecto principal, ejecutarlo normalmente.
1. Correr el proyecto principal

    `
    python manage.py runserver 127.0.0.1:8000
    `

2. Para correr el segundo proyecto cambiar en el archivo .env la variable *MAIN* a False. Correr el segundo servicio en el puerto 8080

    `
    python manage.py runserver 127.0.0.1:8080
    `
    
