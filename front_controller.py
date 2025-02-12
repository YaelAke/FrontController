from flask import Flask, render_template, request
from dispatcher import dispatcher  

app = Flask(__name__)

#Controlador que maneja las vistas según la opción
@app.route('/')
def front_controller():
    opcion = request.args.get("opcion")
    template = dispatcher(opcion)  # Usa el dispatcher para elegir la vista
    return render_template("base.html", content_template=template)


#Manejo de errores
@app.errorhandler(404)
def page_not_found(error):
    return render_template("base.html", content_template="404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
