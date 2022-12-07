from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    mensaje = """
         <h1>Lenguaje de programación III</h1>
        <h2>Evaluación de la Unidad de Competencia 3</h2>
        <h3>Docente: Mg. Flor Elizabeth Cerdán León</h3>
        <h3>Integrantes: </h3>
        <h4>. Baldeon Figueroa Jhon Percy</h4>
        <h4>. Huaman Simeon Victor</h4>
        <h4>. Granados Esteban Adrian Eduardo</h4>
        
        """
    return HttpResponse(mensaje)

