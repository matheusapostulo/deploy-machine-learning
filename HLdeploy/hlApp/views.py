from django.shortcuts import render
from joblib import load


model = load('./modelos/model_lung.joblib')

def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    genero = request.GET['genero']
    idade = request.GET['idade']
    fumante = request.GET['fumante']
    dedos_amarelos = request.GET['dedos_amarelos']
    ansiedade = request.GET['ansiedade']
    pressao = request.GET['pressao']
    doencas_cronicas = request.GET['doencas_cronicas']
    fadiga = request.GET['fadiga']
    alergia = request.GET['alergia']
    chiado = request.GET['chiado']
    alcool= request.GET['alcool']
    tosse = request.GET['tosse']
    falta_ar = request.GET['falta_ar']
    engolir = request.GET['engolir']
    dor_peito = request.GET['dor_peito']

    y_predict = model.predict([[genero, idade, fumante, dedos_amarelos, ansiedade, pressao, doencas_cronicas, fadiga, alergia, chiado, alcool, tosse, falta_ar, engolir, dor_peito]])
    
    print(y_predict)
    print(type(y_predict[0]))
    
    if y_predict[0] == 2:
        y_predict = 'Baseado em suas informações, há 97.5% de possibilidade de você contrair câncer de pulmão!'
    elif y_predict[0] == 1: 
        y_predict = 'Baseado em suas informações, há 97.5% de possibilidade de você NÃO contrair câncer de pulmão!'
    print(y_predict)
    

    return render(request, 'result.html', {'result': y_predict})