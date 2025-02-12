# Front Controller en Python con Flask

Este proyecto implementa el patrón de diseño **Front Controller** en **Python con Flask**, permitiendo que todas las solicitudes sean gestionadas desde un único punto de entrada. Se utiliza un **Dispatcher** para redirigir dinámicamente las vistas en función de un parámetro en la URL.

## Características Principales
- **Control Centralizado:** Todas las solicitudes pasan por un único controlador frontal.  
- **Patrón Front Controller:** La lógica de enrutamiento se mantiene en un solo punto.  
- **Menú Fijo:** La interfaz mantiene una barra de navegación estática que permite cambiar de vista sin necesidad de volver al inicio.  
- **Manejo de Errores 404:** Si se ingresa una opción no válida, se muestra una página de error personalizada.  

## Tecnologías Utilizadas
- **Python 3.x**  
- **Flask** (para manejar el enrutamiento y renderización de plantillas)  
- **HTML + CSS** (para la estructura y diseño de las vistas)  

## Características del Patrón Front Controller
El **Front Controller** es un patrón de diseño que proporciona un único punto de entrada para manejar todas las solicitudes, lo que facilita la seguridad, la autenticación y el enrutamiento en aplicaciones web.  

- **Centralización del Control:** Todas las solicitudes pasan por un único controlador.  
- **Separación de Responsabilidades:** El controlador delega la selección de vistas a un **Dispatcher**.  
- **Escalabilidad:** Es fácil agregar nuevas vistas sin modificar el controlador.  
- **Manejo de Errores:** Se puede gestionar de forma eficiente las solicitudes inválidas.  

## Diagrama de clase UML
![Diagrama UML](https://drive.google.com/uc?export=view&id=1_LzJ2c8-3Ca-zELrFDUrN4il0eC-Avif)
