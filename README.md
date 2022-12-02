# TRABAJO FINAL
# PROGRAMA: "ALUMNOTAS"

## INTRODUCCIÓN
Este programa fue creado dentro del curso de Programación del Centro de Formación Profesional Omar Núñez n° 410 de La Plata, con los conocimientos aprendidos a lo largo de los meses que duró la cursada. Su función consiste en la creación de un diccionario, en el cual se archivará toda la información (simultáneamente se creará un archivo __JSON__ que guardará toda la información que el usuario suba), la _key_ serán el __nombre+apellido__ del alumno, dentro de este diccionario tendremos una lista con valores que serán las __materias__ y guardará las __notas__ correspondientes. Esta información podrá ser consultada por el docente ingresando el nombre y apellido del alumno.
## OBJETIVO DEL PROGRAMA
El objetivo de __ALUMNOTAS__ es facilitarle a los docentes el seguimiento de sus alumnos, pudiendo agregar y conocer sus notas más importantes a la hora de realizar el promedio y así evaluarlos.
## ESTRUCTURA
El código de este programa que trabaja con la interfez gráfica __Tk__ y con un archivo __JSON__ también lo hace con excepciones, parámetros, datos con alcance global y el tipo de lista _ListBox widget_ de _Tkinter_.
## FUNCIONAMIENTO
#### AGREGAR ALUMNOS Y NOTAS
El primer paso para el uso de este programa es llenar al menos las dos primeras casillas a la derecha de "__Alumno:__" y "__Apellido:__" y luego _clickear_ en el botón "__Agregar__". Esto creará un diccionario del cual la _key_ o clave será el nombre y apellido del alumno. En ese mismo momento o después se puede agregar a la derecha de "__Materia:__" y "__Nota:__" el nombre de dicha asignatura y la calificación, las cuales deben agregarse de a una y con números enteros. Al _clickear_ nuevamente en "__Agregar__" esta información se asignará al alumno que se le haya indicado al programa y se guardará.
#### CONSULTAR HISTORIAL
Si uno desea, en cambio, consultar el historial de un alumno, debe colocar el nombre y apellido en los casilleros correspondientes, a la derecha de "__Alumno:__" y "__Apellido:__" y luego _clickear_ en "__Consultar__". Esto abrirá una nueva ventana en la cual se desplegará un listado con el nombre de cada materia y las notas correspondientes de cada una, con el nombre del alumno como título de esta ventana.
#### ELIMINAR INFORMACIÓN
Si uno desea eliminar toda la información guardada, quizás porque ya no está a cargo de los mismos alumnos, simplemente debe _clickear_ en el botón "__Eliminar información__" que figura al abrir el programa. A partir de allí uno ya puede agregar nuevos alumnos.
## FE DE ERRATAS
No funciona con la tecla _enter_ o _intro_, por lo que se debe utilizar el _mouse_ para _clickear_ en los botones que uno desee, en cambio sí funciona la tecla espaciadora para sustituir el _mouse_ con la tecla _tab_ para moverse entre los botones.
## MEJORAS A FUTURO
- __Tecla _enter_:__ se espera pronto habilitar esta función para facilitar el uso del programa sin tener que depender del _mouse_. 
- __Archivar información por años:__ consistiría en poder llevar un seguimiento de los alumnos por años, teniendo en cuenta que hay docentes que están a cargo de cursos por más de un año y también para que este programa también pueda ser utilizado por otro personal de la institución, tales como preceptores y directivos que deseen seguir el recorrido de sus alumnos.
- __Promedio del alumno por materias:__ ayudaría al docente a conocer de manera rápida qué promedio tendrá el alumno.
- __Notas por celdas y formato condicional:__ las notas se verían cada una en su propia celda y ésta se tildaría de rojo en caso de ser igual o inferior a seis (6), indicando que el alumno no ha aprobado ese examen o trabajo. Las demás celdas, con notas aprobadas, quedarán sin color.
