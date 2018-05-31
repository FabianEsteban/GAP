from django.shortcuts import render_to_response, render

def index(request):
    return render_to_response('pages/index.html')

def resultados(request):
    si11 = 0
    no11 = 0
    si21 = 0
    no21 = 0
    si22 = 0
    no22 = 0
    si31 = 0
    no31 = 0
    si32 = 0
    no32 = 0
    si41 = 0
    no41 = 0
    si42 = 0
    no42 = 0
    si43 = 0
    no43 = 0
    cont = 0
    final=[]
    datos=[]
    for x in range(0,33):
        cont = cont + 1
        cont2 = str(cont)
        if cont>0 and cont<8:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si11 = si11 + 1
            else:
                no11 = no11 +1

        if cont>7 and cont<16:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si21 = si21 + 1
            else:
                no21 = no21 + 1

        if cont>15 and cont<19:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si22 = si22 + 1
            else:
                no22 = no22 + 1

        if cont>18 and cont<22:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si31 = si31 + 1
            else:
                no31 = no31 + 1

        if cont>21 and cont<24:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si32 = si32 + 1
            else:
                no32 = no32 + 1

        if cont>23 and cont<28:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si41 = si41 + 1
            else:
                no41 = no41 + 1

        if cont>27 and cont<31:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si42 = si42 + 1
            else:
                no42 = no42 + 1

        if cont>30 and cont<34:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si43 = si43 + 1
            else:
                no43 = no43 + 1

    promedio11 = float("{0:.2f}".format(((si11 * 100)/(si11 + no11))))
    promedio21 = float("{0:.2f}".format(((si21 * 100)/(si21 + no21))))
    promedio22 = float("{0:.2f}".format(((si22 * 100)/(si22 + no22))))
    promedio31 = float("{0:.2f}".format(((si31 * 100)/(si31 + no31))))
    promedio32 = float("{0:.2f}".format(((si32 * 100)/(si32 + no32))))
    promedio41 = float("{0:.2f}".format(((si41 * 100)/(si41 + no41))))
    promedio42 = float("{0:.2f}".format(((si42 * 100)/(si42 + no42))))
    promedio43 = float("{0:.2f}".format(((si43 * 100)/(si43 + no43))))

    promedio2 = float("{0:.2f}".format(((promedio21 + promedio22)/2)))
    promedio3 = float("{0:.2f}".format(((promedio31 + promedio32)/2)))
    promedio4 = float("{0:.2f}".format(((promedio41 + promedio42 + promedio43)/3)))

    if promedio11 <=50:
        consejo11 = "Estay to' cagao"
    else:
        consejo11 = "Sigue así"

    if promedio21 <=50:
        consejo21 = "Estay to' cagao"
    else:
        consejo21 = "Sigue así"

    if promedio22 <=50:
        consejo22 = "Estay to' cagao"
    else:
        consejo22 = "Sigue así"

    if promedio2 <=50:
        consejo2 = "Estay to' cagao"
    else:
        consejo2 = "Sigue así"

    if promedio31 <=50:
        consejo31 = "Estay to' cagao"
    else:
        consejo31 = "Sigue así"

    if promedio32 <=50:
        consejo32 = "Estay to' cagao"
    else:
        consejo32 = "Sigue así"

    if promedio3 <=50:
        consejo3 = "Estay to' cagao"
    else:
        consejo3 = "Sigue así"

    if promedio41 <=50:
        consejo41 = "Estay to' cagao"
    else:
        consejo41 = "Sigue así"

    if promedio42 <=50:
        consejo42 = "Estay to' cagao"
    else:
        consejo42 = "Sigue así"

    if promedio43 <=50:
        consejo43 = "Estay to' cagao"
    else:
        consejo43 = "Sigue así"

    if promedio4 <=50:
        consejo4 = "Estay to' cagao"
    else:
        consejo4 = "Sigue así"

    datos = promedio11, consejo11, promedio21, consejo21, promedio22, consejo22, promedio2, consejo2, promedio31, consejo31, promedio32, consejo32, promedio3, consejo3, promedio41, consejo41, promedio42, consejo42, promedio43, consejo43, promedio4, consejo4

    final.append(datos)

    return render(request, 'pages/resultados.html', {'datos':final})

