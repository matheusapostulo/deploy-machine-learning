from django.shortcuts import render
from joblib import load


model = load('./modelos/model_lung.joblib')

def predictor(request):
    if request.method == 'POST':
        genero = request.POST['genero']
        idade = request.POST['idade']
        fumante = request.POST['fumante']
        dedos_amarelos = request.POST['dedos_amarelos']
        ansiedade = request.POST['ansiedade']
        pressao = request.POST['pressao']
        doencas_cronicas = request.POST['doencas_cronicas']
        fadiga = request.POST['fadiga']
        alergia = request.POST['alergia']
        chiado = request.POST['chiado']
        alcool= request.POST['alcool']
        tosse = request.POST['tosse']
        falta_ar = request.POST['falta_ar']
        engolir = request.POST['engolir']
        dor_peito = request.POST['dor_peito']

        y_predict = model.predict([[genero, idade, fumante, dedos_amarelos, ansiedade, pressao, doencas_cronicas, fadiga, alergia, chiado, alcool, tosse, falta_ar, engolir, dor_peito]])
        
        if y_predict[0] == 2:
            y_predict = 'Baseado em suas informações, há 97.5% de possibilidade de você contrair câncer de pulmão!'
        elif y_predict[0] == 1: 
            y_predict = 'Baseado em suas informações, há 97.5% de possibilidade de você NÃO contrair câncer de pulmão!'
        print(y_predict)
        
        return render(request, 'main.html', {'result': y_predict})

    return render(request, 'main.html')

