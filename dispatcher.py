# Mapea las opciones a las vistas correspondientes.
def dispatcher(opcion):
    """ Mapea las opciones a las vistas correspondientes """
    views = {
        "about": "about.html",
        "contact": "contact.html",
        "profile": "profile.html",
        "inicio": "index.html"
    }
    
    if opcion is None:  
        return "index.html"
    return views.get(opcion, "404.html")  # Si la opción no es válida, devuelve al error 404.html
