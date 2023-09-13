<h1>Tercera Pre-Entrega -- Nishihigahara, Gastón</h1>

#### Objetivo: Desarrollar una WEB Django con patrón MVT subida a Github.

Proyecto Web Django con patrón MVT que incluya:
<ol>
<li> Herencia de HTML.
<li> Por lo menos 3 clases en models.
<li> Un formulario para insertar datos a todas las clases de tu models.
<li> Un formulario para buscar algo en la BD.
<li> Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.
</ol>

### MI PROYECTO (version 0.1)
<p> Funciona como un TO DO LIST. <br>
Es un portal donde se pueden cargar tareas del hogar. A medida que se completan vas ganandos puntos que se pueden canjear (WIP).</p> 

<b> Hay 3 MODELOS: Usuarios | Tareas | Premios. </b>
<p> Se pueden cargar datos de los usuarios, tareas que se pueden completar para ganar puntos. Se pueden cargar premios que pueden ser cambiados por puntos acumulados. <br>Y tenes un buscador para buscar tareas dependiendo de cuanto puntaje queres ganar.</p>


#### Cómo testearlo?
<ul>
<li> Posicionarse en el path del Proyecto [ToDo_List]
<li> Ejecutar "python manage.py runserver" y abrir la dirección IP junto a "appTODO".

- Por ejemplo: `http://123.0.0.2:5000/appTODO/`
<li> Navegar por las 5 opciones del navegador

1. Inicio (Portada / Home).
2. Crear Usuarios. [Nombre | Apellido | Puntos iniciales]
3. Crear Tareas.   [Nombre | Detalle  | Puntos]
4. Crear Premios.  [Premio | Detalle  | Stock | Puntos]
5. Consultar Tareas.
<br>
<li> Ingresar al Menu "Consultar Tareas". 
<p> Se puede ver un listado de las tareas disponibles. <br> Inicialmente hay 3 tareas cargadas. 2 por 100 puntos y 1 por 500. </p>

    Test 01:
    - Input:  Buscar tareas por 50 puntos.
    - Output: Se deben mostrar todos los resultados con más de 50 puntos. <br> Con la base original, se muestran 3 resultados.
<br>

    Test 02:
    - Input:  Buscar tareas por 150 puntos.
    - Output: Se deben mostrar todos los resultados con más de 150 puntos. <br> Con la base original, se muestra 1 solo resultado.
<br>

    Test 03:
    - Input:  Buscar tareas por 600 puntos.
    - Output: Se muestra un cartel que indica que no hay resultados.
<br>

<li> Ingresar al Menu "Crear Usuarios". 

    Test 04:
    - Input:  Completar [Nombre | Apellido | Puntos iniciales] y clickear en Enviar.
    - Output: Se crea una línea en la base de datos "AppTODO_usuarios".
<br>

<li> Ingresar al Menu "Crear Tareas". 

    Test 05:
    - Input:  Completar [Nombre | Detalle  | Puntos] y clickear en Enviar.
    - Output: Se crea una línea en la base de datos "AppTODO_tareas".
<br>

<li> Ingresar al Menu "Crear Premios". 

    Test 06:
    - Input:  Completar [Premio | Detalle  | Stock | Puntos] y clickear en Enviar.
    - Output: Se crea una línea en la base de datos "AppTODO_premios".
<br>