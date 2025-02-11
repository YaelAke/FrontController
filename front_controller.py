from flask import Flask, render_template, request
from dispatcher import dispatcher  

app = Flask(__name__)

@app.route('/')
def front_controller():
    """ Controlador frontal que maneja las vistas según la opción en la URL. """
    opcion = request.args.get("opcion")  
    template = dispatcher(opcion)  # Usa el dispatcher para elegir la vista
    return render_template("base.html", content_template=template)

@app.errorhandler(404)
def page_not_found(error):
    """ Manejo global de errores 404 """
    return render_template("base.html", content_template="404.html"), 404
