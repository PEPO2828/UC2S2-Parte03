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

def primos(request,a,b):
    mensaje = f"""
        <h2>Numeros Primos entre {a} y {b}</h2>
        Resultado :<br> 
        <ul>    
    """
    if a>b:
        for i in range(b,a+1):
            valor= range(2,i)
            contador = 0
            for n in valor:
                if i % n == 0:
                    contador +=1
            if contador <= 0 :
                mensaje += f" <li>{i}</li>"
    else:
        for i in range(a,b+1):
            valor= range(2,i)
            contador = 0
            for n in valor:
                if i % n == 0:
                    contador +=1
            if contador <= 0 :
                mensaje += f" <li>{i}</li>"
    mensaje +="</ul>"
    return HttpResponse(mensaje)



