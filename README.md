# Filmstorage

## Descripción

**Filmstorage** es una página web que busca una funcionalidad similar a la de los antiguos videoclubs. Es decir, permitir a los usuarios realizar préstamos sobre determinados filmes o contenido audiovisual en general. El almacenamiento de los datos se basa en el filtrado y creación de las películas basado en 4 clases principales (Director, Actor, Género, Película y Préstamo). Así, los usuarios tratan directamente sobre los préstamos, actuando estos como forma tratable de la información, siendo la representación de un ejemplar concreto de una película solicitable por los usuarios.

### Relaciones entre las clases

La clase dedicada a los préstamos obtiene como clave ajena el título de la película de la cual es un ejemplar. Una vez dentro de la película, ésta obtiene como claves ajenas el director de la misma, el género principal al que pertenece y su protagonista. Así quedarían resumidas las relaciones entre ellas.

### Funcionalidad de la Página

La página permite a los empleados de Filmstorage crear, modificar y eliminar ejemplares de su base de datos, así como a los usuarios observar el catálogo de la página y observar los ejemplares solicitados junto con la fecha establecida de devolución. Además, los usuarios podrán solicitar la asignación de un préstamo a los empleados mediante un formulario de contacto.

### Instalación del Servicio

La instalación del servicio es sencilla. Deberá realizarse la descarga del mismo y un entorno python sobre el que pueda funcionar. Importando los requerimentos del fichero **requirements.txt** y ativando el servicio, la página estará lista para su uso. Para acceder a ella simplemente se deberá introducir la dirección IP asignada en el navegador. 

Las prestaciones para el usuario administrador y los clientes serán distintas, por lo que se proporcionará el usuario administrador "admin" con contraseña "SGzj{3PX"