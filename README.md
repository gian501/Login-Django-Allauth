Este proyecto es la continuación en una serie con el objetivo de desarrollar paginas web que puedan contener la mejor calidad de información y le permitan al usuario mayores facilidades y posibilidades.

Mediante el desarrollo web utilizando HTML5 y CSS  realizamos una maquetación muy sencilla. Esto nos da posibilidades infinitas para el día de mañana poder reciclarlo. Este pequeño blog que no esta totalmente terminado, tiene el objetivo de  poder realizar un login de usuarios mediante distintas redes sociales y poder administrar la información mediante el panel de admin, con relaciones Uno a uno, como  es en este caso Google. Con posterioridad iremos agregando servicios, ya sea Facebook, LinkedIn y otros. 

Para el caso en concreto, utilizamos el lenguaje Python con Django y las librerías de Allauth.



Que es AllAuth?



Es una aplicación de autenticación completamente integrada que permita la verificación tanto local como social, con flujos que simplemente funcionan, maravillosamente.

Como sabremos, desafortunadamente, la mayoría de las aplicaciones de Django existentes que abordan el problema de la autenticación social se enfocan solo en una dimensión: la social. La mayoría de los desarrolladores terminan integrando otra aplicación para admitir los flujos de autenticación que se generan localmente.

Este enfoque crea una brecha de desarrollo entre los flujos de autenticación locales y sociales. Ha seguido siendo un problema a pesar de los numerosos escenarios comunes que ambos requieren.

Por ejemplo, es posible que no se verifique una dirección de correo electrónico proporcionada por un proveedor de OpenID. Por lo tanto, antes de cônectar una cuenta OpeniD a una cuenta local, se debe verificar la dirección de correo electrónico. Este es esencialmente uno de los muchos casos de uso que exigen que la verificación de correo electrónico esté presente en ambos mundos.

Integrar ambos es un proceso enorme y tedioso. No es tan simple como agregar una aplicación de autenticación social y una aplicación de registro de cuenta local a su INSTALLED_APPS lista.



Características :

Admite múltiples esquemas de autenticación (p. ej., inicio de sesión por nombre de usuario o por correo electrónico), así como múltiples estrategias para la verificación de cuentas (desde ninguna hasta verificación por correo electrónico).
  Todos los tokens de acceso se almacenan constantemente para que pueda publicar  actualizaciones de muros, etc.




Diseño arquitectónico

  Formulario de registro conectable para hacer preguntas adicionales durante el registro.
  Soporte para conectar varias cuentas sociales a una cuenta de usuario de Django ( Para el caso en concreto Google).
  Las claves y los secretos del consumidor requeridos para interactuar con Facebook, Twitter y similares deben configurarse en la base de datos a través del administrador de Django utilizando el modelo SocialApp.
  Las claves de consumo, los tokens hacen uso del marco de sitios de Django. Esto es especialmente útil para proyectos más grandes de múltiples dominios, pero también permite cambiar fácilmente entre una configuración de desarrollo (host local) y producción sin alterar la configuración y la base de datos.


El primer proveedor que utilizamos fue Google, pero con posterioridad agregaremos Facebook y LinkedIn



A través de los formularios creados podríamos registrar un usuario nuevo para el cual se Utilizó CrispyForms para mejorarlo y posteriormente que el usuario pueda loquearse. Esto nos permitirá estar registrados como usuarios dentro de la base de datos y poder ingresar a la página para ver los productos. Allauth, nos permite no solo la verificación, sino también almacenar los datos como nombre, apellido y email de los distintos proveedores, haciendo que estos datos ya estén incluidos en el perfil. 



Se realizo un requiremets.txt Para especificar al instalar que necesita para hacer correr el programa. 





Por razones de seguridad se debió borrar las credenciales de google.
