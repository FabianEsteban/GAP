from django.shortcuts import render_to_response, render, redirect
from page.forms import CodigoForm, SignUpForm
from page.models import Codigo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


def index(request):
    return render_to_response('pages/index.html')

@login_required()
def empresa(request):
    usuario = request.user.__str__
    return render_to_response('pages/empresa.html', {'usuario':usuario})

@login_required()
def administrador(request):
    usuario = request.user.__str__
    return render_to_response('pages/administrador.html', {'usuario':usuario})

@login_required()
def signup(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid() :
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        user = User.objects.get(username=username)
        user.set_password(raw_password)
        user.is_staff = False
        user.save()
        user.groups.add(Group.objects.get(name='Empresas'))
        return redirect('ingreso')

    else:
        form = SignUpForm()
    return render(request, 'pages/signup.html', {'form': form})

@login_required()
def ingreso(request):
    if request.user.groups.filter(name='Empresas').exists():
        usuario = request.user.__str__
        cantidad = str(request.user.last_name)
        cantidad2 = int(cantidad)
        return render_to_response('pages/empresa.html', {'cantidad':cantidad2, 'usuario':usuario})
    if request.user.groups.filter(name='Administradores').exists():
        usuario = request.user.__str__
        return render_to_response('pages/administrador.html', {'usuario':usuario})


def error_500(request):
    data = {}
    return render(request,'pages/500.html', data)

@login_required()
def preguntas(request):
    form = CodigoForm
    return render_to_response('pages/preguntas.html', {'form': form})

@login_required()
def promedio(request):
    ingresado = request.user
    datos = Codigo.objects.filter(codigo=ingresado)

    cont = 0
    final11 = 0
    final2 = 0
    final21 = 0
    final22 = 0
    final3 = 0
    final31 = 0
    final32 = 0
    final4 = 0
    final41 = 0
    final42 = 0
    final43 = 0
    final5 = 0
    final51 = 0
    final52 = 0
    final6 = 0
    final61 = 0
    final62 = 0
    final63 = 0
    final64 = 0
    final65 = 0
    final66 = 0
    final67 = 0
    final68 = 0
    final69 = 0
    final610 = 0
    final7 = 0
    final71 = 0
    final72 = 0
    final73 = 0
    final74 = 0
    final75 = 0
    final76 = 0
    final77 = 0
    final8 = 0
    final81 = 0
    final82 = 0
    final83 = 0
    final84 = 0
    final85 = 0
    final86 = 0
    final9 = 0
    final91 = 0
    final92 = 0
    final10 = 0
    final101 = 0
    final011 = 0
    final111 = 0
    final112 = 0
    final113 = 0

    contador=[]
    promedio11=[]
    promedio2=[]
    promedio21=[]
    promedio22=[]
    promedio3=[]
    promedio31=[]
    promedio32=[]
    promedio4=[]
    promedio41=[]
    promedio42=[]
    promedio43=[]
    promedio5=[]
    promedio51=[]
    promedio52=[]
    promedio6=[]
    promedio61=[]
    promedio62=[]
    promedio63=[]
    promedio64=[]
    promedio65=[]
    promedio66=[]
    promedio67=[]
    promedio68=[]
    promedio69=[]
    promedio610=[]
    promedio7=[]
    promedio71=[]
    promedio72=[]
    promedio73=[]
    promedio74=[]
    promedio75=[]
    promedio76=[]
    promedio77=[]
    promedio8=[]
    promedio81=[]
    promedio82=[]
    promedio83=[]
    promedio84=[]
    promedio85=[]
    promedio86=[]
    promedio9=[]
    promedio91=[]
    promedio92=[]
    promedio10=[]
    promedio101=[]
    promedio011=[]
    promedio111=[]
    promedio112=[]
    promedio113=[]

    final=[]

    for x in datos:
        cont = cont + 1
        promedio11.append(x.promedio11)
        promedio2.append(x.promedio2)
        promedio21.append(x.promedio21)
        promedio22.append(x.promedio22)
        promedio3.append(x.promedio3)
        promedio31.append(x.promedio31)
        promedio32.append(x.promedio32)
        promedio4.append(x.promedio4)
        promedio41.append(x.promedio41)
        promedio42.append(x.promedio42)
        promedio43.append(x.promedio43)
        promedio5.append(x.promedio5)
        promedio51.append(x.promedio51)
        promedio52.append(x.promedio52)
        promedio6.append(x.promedio6)
        promedio61.append(x.promedio61)
        promedio62.append(x.promedio62)
        promedio63.append(x.promedio63)
        promedio64.append(x.promedio64)
        promedio65.append(x.promedio65)
        promedio66.append(x.promedio66)
        promedio67.append(x.promedio67)
        promedio68.append(x.promedio68)
        promedio69.append(x.promedio69)
        promedio610.append(x.promedio610)
        promedio7.append(x.promedio7)
        promedio71.append(x.promedio71)
        promedio72.append(x.promedio72)
        promedio73.append(x.promedio73)
        promedio74.append(x.promedio74)
        promedio75.append(x.promedio75)
        promedio76.append(x.promedio76)
        promedio77.append(x.promedio77)
        promedio8.append(x.promedio8)
        promedio81.append(x.promedio81)
        promedio82.append(x.promedio82)
        promedio83.append(x.promedio83)
        promedio84.append(x.promedio84)
        promedio85.append(x.promedio85)
        promedio86.append(x.promedio86)
        promedio9.append(x.promedio9)
        promedio91.append(x.promedio91)
        promedio92.append(x.promedio92)
        promedio10.append(x.promedio10)
        promedio101.append(x.promedio101)
        promedio011.append(x.promedio011)
        promedio111.append(x.promedio111)
        promedio112.append(x.promedio112)
        promedio113.append(x.promedio113)

    for i in promedio11:
        final11 = final11 + int(float(i))
    final11 = float("{0:.2f}".format(final11/len(promedio11)))

    for i in promedio2:
        final2 = final2 + int(float(i))
    final2 = float("{0:.2f}".format(final2/len(promedio2)))

    for i in promedio21:
        final21 = final21 + int(float(i))
    final21 = float("{0:.2f}".format(final21/len(promedio21)))

    for i in promedio22:
        final22 = final22 + int(float(i))
    final22 = float("{0:.2f}".format(final22/len(promedio22)))

    for i in promedio3:
        final3 = final3 + int(float(i))
    final3 = float("{0:.2f}".format(final3/len(promedio3)))

    for i in promedio31:
        final31 = final31 + int(float(i))
    final31 = float("{0:.2f}".format(final31/len(promedio31)))

    for i in promedio32:
        final32 = final32 + int(float(i))
    final32 = float("{0:.2f}".format(final32/len(promedio32)))

    for i in promedio4:
        final4 = final4 + int(float(i))
    final4 = float("{0:.2f}".format(final4/len(promedio4)))

    for i in promedio41:
        final41 = final41 + int(float(i))
    final41 = float("{0:.2f}".format(final41/len(promedio41)))

    for i in promedio42:
        final42 = final42 + int(float(i))
    final42 = float("{0:.2f}".format(final42/len(promedio42)))

    for i in promedio43:
        final43 = final43 + int(float(i))
    final43 = float("{0:.2f}".format(final43/len(promedio43)))

    for i in promedio5:
        final5 = final5 + int(float(i))
    final5 = float("{0:.2f}".format(final5/len(promedio5)))

    for i in promedio51:
        final51 = final51 + int(float(i))
    final51 = float("{0:.2f}".format(final51/len(promedio51)))

    for i in promedio52:
        final52 = final52 + int(float(i))
    final52 = float("{0:.2f}".format(final52/len(promedio52)))

    for i in promedio6:
        final6 = final6 + int(float(i))
    final6 = float("{0:.2f}".format(final6/len(promedio6)))

    for i in promedio61:
        final61 = final61 + int(float(i))
    final61 = float("{0:.2f}".format(final61/len(promedio61)))

    for i in promedio62:
        final62 = final62 + int(float(i))
    final62 = float("{0:.2f}".format(final62/len(promedio62)))

    for i in promedio63:
        final63 = final63 + int(float(i))
    final63 = float("{0:.2f}".format(final63/len(promedio63)))

    for i in promedio64:
        final64 = final64 + int(float(i))
    final64 = float("{0:.2f}".format(final64/len(promedio64)))

    for i in promedio65:
        final65 = final65 + int(float(i))
    final65 = float("{0:.2f}".format(final65/len(promedio65)))

    for i in promedio66:
        final66 = final66 + int(float(i))
    final66 = float("{0:.2f}".format(final66/len(promedio66)))

    for i in promedio67:
        final67 = final67 + int(float(i))
    final67 = float("{0:.2f}".format(final67/len(promedio67)))

    for i in promedio68:
        final68 = final68 + int(float(i))
    final68 = float("{0:.2f}".format(final68/len(promedio68)))

    for i in promedio69:
        final69 = final69 + int(float(i))
    final69 = float("{0:.2f}".format(final69/len(promedio69)))

    for i in promedio610:
        final610 = final610 + int(float(i))
    final610 = float("{0:.2f}".format(final610/len(promedio610)))

    for i in promedio7:
        final7 = final7 + int(float(i))
    final7 = float("{0:.2f}".format(final7/len(promedio7)))

    for i in promedio71:
        final71 = final71 + int(float(i))
    final71 = float("{0:.2f}".format(final71/len(promedio71)))

    for i in promedio72:
        final72 = final72 + int(float(i))
    final72 = float("{0:.2f}".format(final72/len(promedio72)))

    for i in promedio73:
        final73 = final73 + int(float(i))
    final73 = float("{0:.2f}".format(final73/len(promedio73)))

    for i in promedio74:
        final74 = final74 + int(float(i))
    final74 = float("{0:.2f}".format(final74/len(promedio74)))

    for i in promedio75:
        final75 = final75 + int(float(i))
    final75 = float("{0:.2f}".format(final75/len(promedio75)))

    for i in promedio76:
        final76 = final76 + int(float(i))
    final76 = float("{0:.2f}".format(final76/len(promedio76)))

    for i in promedio77:
        final77 = final77 + int(float(i))
    final77 = float("{0:.2f}".format(final77/len(promedio77)))

    for i in promedio8:
        final8 = final8 + int(float(i))
    final8 = float("{0:.2f}".format(final8/len(promedio8)))

    for i in promedio81:
        final81 = final81 + int(float(i))
    final81 = float("{0:.2f}".format(final81/len(promedio81)))

    for i in promedio82:
        final82 = final82 + int(float(i))
    final82 = float("{0:.2f}".format(final82/len(promedio82)))

    for i in promedio83:
        final83 = final83 + int(float(i))
    final83 = float("{0:.2f}".format(final83/len(promedio83)))

    for i in promedio84:
        final84 = final84 + int(float(i))
    final84 = float("{0:.2f}".format(final84/len(promedio84)))

    for i in promedio85:
        final85 = final85 + int(float(i))
    final85 = float("{0:.2f}".format(final85/len(promedio85)))

    for i in promedio86:
        final86 = final86 + int(float(i))
    final86 = float("{0:.2f}".format(final86/len(promedio86)))

    for i in promedio9:
        final9 = final9 + int(float(i))
    final9 = float("{0:.2f}".format(final9/len(promedio9)))

    for i in promedio91:
        final91 = final91 + int(float(i))
    final91 = float("{0:.2f}".format(final91/len(promedio91)))

    for i in promedio92:
        final92 = final92 + int(float(i))
    final92 = float("{0:.2f}".format(final92/len(promedio92)))

    for i in promedio10:
        final10 = final10 + int(float(i))
    final10 = float("{0:.2f}".format(final10/len(promedio10)))

    for i in promedio101:
        final101 = final101 + int(float(i))
    final101 = float("{0:.2f}".format(final101/len(promedio101)))

    for i in promedio011:
        final011 = final011 + int(float(i))
    final011 = float("{0:.2f}".format(final011/len(promedio011)))

    for i in promedio111:
        final111 = final111 + int(float(i))
    final111 = float("{0:.2f}".format(final111/len(promedio111)))

    for i in promedio112:
        final112 = final112 + int(float(i))
    final112 = float("{0:.2f}".format(final112/len(promedio112)))

    for i in promedio113:
        final113 = final113 + int(float(i))
    final113 = float("{0:.2f}".format(final113/len(promedio113)))

    if final11 <=75:
        consejo11 = "Se sugiere controlar las políticas de seguridad de la organización con el documento de política de seguridad. En caso de no existir el documento, se debe elaborar tomando en cuenta los conceptos de política de información."
    else:
        consejo11 = "Sigue así, no olvides controlar las políticas de seguridad constantemente considerando los departamentos partícipes."

    if final2 <=75:
        consejo2 = ""
    else:
        consejo2 = "Sigue así"

    if final21 <=75:
        consejo21 = "Se sugiere establecer una estructura para la gestión de la organización. Para lograr esto, cada punto organizacional debe ser bien asignado tanto los roles como las responsabilidades que cumple cada uno, siempre teniendo presente la confidencialidad de la información."
    else:
        consejo21 = "La coordinación de actividades de la seguridad informática están bien definidos, recuerda de igual manera revisar los roles y responsabilidades."

    if final22 <=75:
        consejo22 = "Se recomienda identificar los riesgos de terceros que involucran la interacción con la información de la organización para así controlarlos apropiadamente antes de permitir el acceso. También, se recomienda revisar que los requisitos de seguridad sean cumplidos por terceros. Por otro lado,se  advierte realizar una revisión exhaustiva de los procesos, comunicaciones, información, productos o servicios llevados a cabo con terceros, para verificar si se cumplen los requisitos de seguridad."
    else:
        consejo22 = "Cumpliste con la identificación de tus requisitos de seguridad y riesgos, ahora debes establecer un acuerdo con terceros que los involucre. "

    if final3 <=75:
        consejo3 = ""
    else:
        consejo3 = "Sigue así"

    if final31 <=75:
        consejo31 = "Se sugiere llevar un catastro de todos los activos y sus respectivos dueños. (directivos o gestores responsables de proteger sus activos). Para así llevar un registro de cada activo importante de la empresa y los detalles relevantes de ellos."
    else:
        consejo31 = "La identificación, control y regulación que realizaste a los activos asociados están correctas en un porcentaje pero debes mejorar la importancia de aquello."

    if final32 <=75:
        consejo32 = "Se recomienda clasificar la información en términos de requisitos legales, sensibilidad y la criticidad de la organización."
    else:
        consejo32 = "Creaste una guía de clasificación, etiquetaste y manejaste la información. No olvidaste esquematizar de acuerdo a tu organización."

    if final4 <=75:
        consejo4 = ""
    else:
        consejo4 = "Sigue así"

    if final41 <=75:
        consejo41 = "Se recomienda comunicar y documentar claramente los roles y la responsabilidad de cada persona previa a la contratación en la organización. También, se recomienda firmar acuerdos de confidencialidad y no divulgación de información a cada empleado, contratista o tercero que trabaje en la organización."
    else:
        consejo41 = "Sigue así"

    if final42 <=75:
        consejo42 = "Se recomienda preestablecer proceso formal de acción para sanciones a los empleados que hayan cometido una falta de seguridad.También, se debe contratar personal que cuente con los conocimientos necesarios sobre seguridad informática para  llevar a cabo entrenamientos al personal de la organización. Lo anterior considerando que no existe personal calificado. "
    else:
        consejo42 = "Sigue así"

    if final43 <=75:
        consejo43 = "Se sugiere eliminar los derechos de acceso debido a que el o los recursos humanos que ya no son parte de la organización, pudiesen divulgar información confidencial que traería consecuencias a la empresa. También, se recomienda establecer proceso de devolución de activos. Por ejemplo, en el ámbito de término de relación laboral, termino de contrato o finalización de acuerdo."
    else:
        consejo43 = "Sigue así"

    if final5 <=75:
        consejo5 = ""
    else:
        consejo5 = "Sigue así"

    if final51 <=75:
        consejo51 = "Se recomienda restringir el acceso a personal no autorizado o desconocido a la organización y establecer políticas de  seguridad física como el uso de candados para resguardar activos que contengan seguridad confidencial de la organización."
    else:
        consejo51 = "Sigue así"

    if final52 <=75:
        consejo52 = "Se sugiere identificar las potenciales amenazas y vulnerabilidades que atenten contra la seguridad de equipos, como también, sus respectivas respuestas a dichas amenazas.  "
    else:
        consejo52 = "Sigue así"

    if final6 <=75:
        consejo6 = ""
    else:
        consejo6 = "Sigue así"

    if final61 <=75:
        consejo61 = "Se sugiere llevar un control de cambios exhaustivo. También, que cada proceso operacional esté debidamente documentado para los usuarios que lo necesiten. Finalmente,  separar la facilidad de desarrollo con las facilidad operacional."
    else:
        consejo61 = "Sigue así"

    if final62 <=75:
        consejo62 = "Se recomienda monitorear, registrar y llevar auditoría de mediciones de registro."
    else:
        consejo62 = "Sigue así"

    if final63 <=75:
        consejo63 = "Se sugiere llevar a cabo una planeación que asegure la capacidad y disponibilidad de recursos necesarios para una proyección futura."
    else:
        consejo63 = "Sigue así"

    if final64 <=75:
        consejo64 = "Se sugiere realizar una exhaustiva revisión de los códigos maliciosos como también utilizar programas que resguarden la información y permitan contrarrestar malware."
    else:
        consejo64 = "Sigue así"

    if final65 <=75:
        consejo65 = ""
    else:
        consejo65 = "Sigue así"

    if final66 <=75:
        consejo66 = "Se recomienda tener control sobre la detección, prevención y control para así protegerse contra código malicioso como también para código móvil."
    else:
        consejo66 = "Sigue así"

    if final67 <=75:
        consejo67 = "Sería óptimo generar procedimientos respecto a los medios removibles, proteger la documentación en sistemas y desechar aquellos que no son requeridos en forma formal. "
    else:
        consejo67 = "Sigue así"

    if final68 <=75:
        consejo68 = "El intercambio de información debe conllevar una política, acuerdos, contenido de seguridad y protección ante accesos no autorizados tanto como en los medios que contienen la información y mensajería."
    else:
        consejo68 = "Sigue así"

    if final69 <=75:
        consejo69 = "Se recomienda realizar documento el cual compromete a ambas partes a los términos de comercio incluyendo detalladamente los temas de seguridad. También, la integridad de la información pública disponible debe estar protegida contra las modificaciones no autorizadas."
    else:
        consejo69 = "Sigue así"

    if final610 <=75:
        consejo610 = "Se sugiere monitorear los sistemas y los informes de incidentes relacionados a las seguridad de la información "
    else:
        consejo610 = "Sigue así"

    if final7 <=75:
        consejo7 = ""
    else:
        consejo7 = "Sigue así"

    if final71 <=75:
        consejo71 = "Se sugiere revisar las políticas de control de acceso y además informar tanto a usuarios como proveedores los requisitos del negocio que deben ser cumplidos respecto al control de acceso."
    else:
        consejo71 = "Sigue así"

    if final72 <=75:
        consejo72 = "Se sugiere especificar procedimientos formales para controlar los derechos de acceso.Los procedimientos deben estar presentes desde el registro de un nuevo usuario hasta el borrado del mismo."
    else:
        consejo72 = "Sigue así"

    if final73 <=75:
        consejo73 = "Se sugiere concientizar al usuario que forma parte fundamental de la seguridad dentro de la organización."
    else:
        consejo73 = "Sigue así"

    if final74 <=75:
        consejo74 = "Mejorar"
    else:
        consejo74 = "Sigue así"

    if final75 <=75:
        consejo75 = "Se considerará el uso de medios de seguridad para restringir el acceso a usuarios no autorizados.Además se deben llevar a cabo procedimientos de seguridad como por ejemplo, el registro de intentos fallidos y exitosos de autenticación del sistema."
    else:
        consejo75 = "Sigue así"

    if final76 <=75:
        consejo76 = "Se sugiere proporcionar protección ante accesos no autorizado relacionados con las políticas de seguridad establecidas."
    else:
        consejo76 = "Sigue así"

    if final77 <=75:
        consejo77 = "Se sugiere en primer lugar, identificar si la actividad de teletrabajo se encuentra autorizada y controlada por la adminsitración.De ser así, otorgar los permisos para realizar el trabajo de dicha forma."
    else:
        consejo77 = "Sigue así"

    if final8 <=75:
        consejo8 = "Se sugiere identificar los requisitos de seguridad antes del desarrollo e implementación para que así puedan ser protegidos para el mantenimiento de su confidencialidad, autenticidad o integridad. "
    else:
        consejo8 = "Sigue así"

    if final81 <=75:
        consejo81 = "Se sugiere que antes de desarrollar los sistemas de información, se debe identificar y acordar los requisitos de seguridad."
    else:
        consejo81 = "Sigue así"

    if final82 <=75:
        consejo82 = "Se sugiere llevar a cabo controles de seguridad en los procesos de aplicaciones como el uso de validaciones de datos de entrada y de salida."
    else:
        consejo82 = "Sigue así"

    if final83 <=75:
        consejo83 = "Se sugiere establecer políticas de seguridad criptográficas para resguardar la autenticidad,confidencialidad e integridad. "
    else:
        consejo83 = "Sigue así"

    if final84 <=75:
        consejo84 = "Se sugiere mantener resguardado el acceso a los sistemas de archivos como también su código fuente."
    else:
        consejo84 = "Sigue así"

    if final85 <=75:
        consejo85 = "Se sugiere llevar a cabo un mantenimiento en la seguridad del software. "
    else:
        consejo85 = "Sigue así"

    if final86 <=75:
        consejo86 = "Se sugiere llevar a cabo una gestión de vulnerabilidad técnica de riesgos que acontezcan de la explotación de dichas vulnerabilidades. "
    else:
        consejo86 = "Sigue así"

    if final9 <=75:
        consejo9 = "Establecer procedimientos formales de registro para notificar eventos que atenten sobre la seguridad informática dentro de la empresa."
    else:
        consejo9 = "Sigue así"

    if final91 <=75:
        consejo91 = "Se sugiere comunicar los eventos y debilidades relacionadas a la seguridad para posteriormente aplicar medidas correctivas.Además establecer procedimientos formales de informe sobre dichos eventos."
    else:
        consejo91 = "Sigue así"

    if final92 <=75:
        consejo92 = "Se considerará el establecimiento de responsabilidades y procedimientos para gestionar los incidentes dentro de la organización.Además se debe buscar la mejora de la seguridad informática dentro de la organización, aplicando procedimientos continuos de monitoreo y evaluación."
    else:
        consejo92 = "Sigue así"

    if final10 <=75:
        consejo10 = ""
    else:
        consejo10 = "Sigue así"

    if final101 <=75:
        consejo101 = "Se sugiere desarrollar e implementar la planificación de continuidad de negocios. Con esto se busca impedir la suspensión de las actividades."
    else:
        consejo101 = "Sigue así"

    if final011 <=75:
        consejo011 = ""
    else:
        consejo011 = "Sigue así"

    if final111 <=75:
        consejo111 = "Se recomienda tener asesoramiento legal capacitado para evitar la violación de cualquier aspecto legal."
    else:
        consejo111 = "Sigue así"

    if final112 <=75:
        consejo112 = "Se recomienda la revisión del cumplimiento técnico este tiene que ser revisado por personal competente y autorizado. También, que la gerencia asegure los procedimientos de seguridad para lograr cumplimiento con las políticas y estándares de seguridad."
    else:
        consejo112 = "Sigue así"

    if final113 <=75:
        consejo113 = "Se recomienda que los requisitos de auditoría y alcance hayan sido acordados con la gerencia apropiada. También, controlar el acceso a las herramientas de auditorías del software de datos son protegidos para prevenir posible mal uso o compromisos.   "
    else:
        consejo113 = "Sigue así"

    info = final11, consejo11, final2, consejo2, final21, consejo21, final22, consejo22, final3, consejo3, final31, consejo31, final32, consejo32, final4, consejo4, final41, consejo41, final42, consejo42, final43, consejo43, final5, consejo5, final51, consejo51, final52, consejo52, final6, consejo6, final61, consejo61, final62, consejo62, final63, consejo63, final64, consejo64, final65, consejo65, final66, consejo66, final67, consejo67, final68, consejo68, final69, consejo69, final610, consejo610, final7, consejo7, final71, consejo71, final72, consejo72, final73, consejo73, final74, consejo74, final75, consejo75, final76, consejo76, final77, consejo77, final8, consejo8, final81, consejo81, final82, consejo82, final83, consejo83, final84, consejo84, final85, consejo85, final86, consejo86, final9, consejo9, final91, consejo91, final92, consejo92, final10, consejo10, final101, consejo101, final011, consejo011, final111, consejo111, final112, consejo112, final113, consejo113
    final.append(info)
    contador.append(cont)

    return render_to_response('pages/promedio.html', {'datos':final, 'contador':contador})

@login_required()
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
    si51 = 0
    no51 = 0
    si52 = 0
    no52 = 0
    si61 = 0
    no61 = 0
    si62 = 0
    no62 = 0
    si63 = 0
    no63 = 0
    si64 = 0
    no64 = 0
    si65 = 0
    no65 = 0
    si66 = 0
    no66 = 0
    si67 = 0
    no67 = 0
    si68 = 0
    no68 = 0
    si69 = 0
    no69 = 0
    si610 = 0
    no610 = 0
    si71 = 0
    no71 = 0
    si72 = 0
    no72 = 0
    si73 = 0
    no73 = 0
    si74 = 0
    no74 = 0
    si75 = 0
    no75 = 0
    si76 = 0
    no76 = 0
    si77 = 0
    no77 = 0
    si81 = 0
    no81 = 0
    si82 = 0
    no82 = 0
    si83 = 0
    no83 = 0
    si84 = 0
    no84 = 0
    si85 = 0
    no85 = 0
    si86 = 0
    no86 = 0
    si91 = 0
    no91 = 0
    si92 = 0
    no92 = 0
    si101 = 0
    no101 = 0
    si111 = 0
    no111 = 0
    si112 = 0
    no112 = 0
    si113 = 0
    no113 = 0
    cont = 0
    final=[]
    datos=[]
    for x in range(0,211):
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

        if cont>33 and cont<41:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si51 = si51 + 1
            else:
                no51 = no51 + 1

        if cont>40 and cont<55:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si52 = si52 + 1
            else:
                no52 = no52 + 1

        if cont>54 and cont<61:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si61 = si61 + 1
            else:
                no61 = no61 + 1

        if cont>60 and cont<65:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si62 = si62 + 1
            else:
                no62 = no62 + 1

        if cont>64 and cont<68:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si63 = si63 + 1
            else:
                no63 = no63 + 1

        if cont>67 and cont<72:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si64 = si64 + 1
            else:
                no64 = no64 + 1

        if cont>71 and cont<74:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si65 = si65 + 1
            else:
                no65 = no65 + 1

        if cont>73 and cont<78:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si66 = si66 + 1
            else:
                no66 = no66 + 1

        if cont>77 and cont<84:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si67 = si67 + 1
            else:
                no67 = no67 + 1

        if cont>83 and cont<89:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si68 = si68 + 1
            else:
                no68 = no68 + 1

        if cont>88 and cont<94:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si69 = si69 + 1
            else:
                no69 = no69 + 1

        if cont>93 and cont<104:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si610 = si610 + 1
            else:
                no610 = no610 + 1

        if cont>103 and cont<107:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si71 = si71 + 1
            else:
                no71 = no71 + 1

        if cont>106 and cont<111:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si72 = si72 + 1
            else:
                no72 = no72 + 1

        if cont>110 and cont<113:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si73 = si73 + 1
            else:
                no73 = no73 + 1

        if cont>112 and cont<124:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si74 = si74 + 1
            else:
                no74 = no74 + 1

        if cont>123 and cont<131:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si75 = si75 + 1
            else:
                no75 = no75 + 1

        if cont>130 and cont<133:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si76 = si76 + 1
            else:
                no76 = no76 + 1

        if cont>132 and cont<137:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si77 = si77 + 1
            else:
                no77 = no77 + 1

        if cont>136 and cont<140:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si81 = si81 + 1
            else:
                no81 = no81 + 1

        if cont>139 and cont<147:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si82 = si82 + 1
            else:
                no82 = no82 + 1

        if cont>146 and cont<155:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si83 = si83 + 1
            else:
                no83 = no83 + 1

        if cont>154 and cont<159:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si84 = si84 + 1
            else:
                no84 = no84 + 1

        if cont>158 and cont<168:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si85 = si85 + 1
            else:
                no85 = no85 + 1

        if cont>167 and cont<170:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si86 = si86 + 1
            else:
                no86 = no86 + 1

        if cont>169 and cont<173:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si91 = si91 + 1
            else:
                no91 = no91 + 1

        if cont>172 and cont<181:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si92 = si92 + 1
            else:
                no92 = no92 + 1

        if cont>180 and cont<191:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si101 = si101 + 1
            else:
                no101 = no101 + 1

        if cont>190 and cont<204:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si111 = si111 + 1
            else:
                no111 = no111 + 1

        if cont>203 and cont<208:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si112 = si112 + 1
            else:
                no112 = no112 + 1

        if cont>207 and cont<212:
            pregunta = request.GET.get(cont2)
            if pregunta == 'Si':
                si113 = si113 + 1
            else:
                no113 = no113 + 1

    promedio11 = float("{0:.2f}".format(((si11 * 100)/(si11 + no11))))
    promedio21 = float("{0:.2f}".format(((si21 * 100)/(si21 + no21))))
    promedio22 = float("{0:.2f}".format(((si22 * 100)/(si22 + no22))))
    promedio31 = float("{0:.2f}".format(((si31 * 100)/(si31 + no31))))
    promedio32 = float("{0:.2f}".format(((si32 * 100)/(si32 + no32))))
    promedio41 = float("{0:.2f}".format(((si41 * 100)/(si41 + no41))))
    promedio42 = float("{0:.2f}".format(((si42 * 100)/(si42 + no42))))
    promedio43 = float("{0:.2f}".format(((si43 * 100)/(si43 + no43))))
    promedio51 = float("{0:.2f}".format(((si51 * 100)/(si51 + no51))))
    promedio52 = float("{0:.2f}".format(((si52 * 100)/(si52 + no52))))
    promedio61 = float("{0:.2f}".format(((si61 * 100)/(si61 + no61))))
    promedio62 = float("{0:.2f}".format(((si62 * 100)/(si62 + no62))))
    promedio63 = float("{0:.2f}".format(((si63 * 100)/(si63 + no63))))
    promedio64 = float("{0:.2f}".format(((si64 * 100)/(si64 + no64))))
    promedio65 = float("{0:.2f}".format(((si65 * 100)/(si65 + no65))))
    promedio66 = float("{0:.2f}".format(((si66 * 100)/(si66 + no66))))
    promedio67 = float("{0:.2f}".format(((si67 * 100)/(si67 + no67))))
    promedio68 = float("{0:.2f}".format(((si68 * 100)/(si68 + no68))))
    promedio69 = float("{0:.2f}".format(((si69 * 100)/(si69 + no69))))
    promedio610 = float("{0:.2f}".format(((si610 * 100)/(si610 + no610))))
    promedio71 = float("{0:.2f}".format(((si71 * 100)/(si71 + no71))))
    promedio72 = float("{0:.2f}".format(((si72 * 100)/(si72 + no72))))
    promedio73 = float("{0:.2f}".format(((si73 * 100)/(si73 + no73))))
    promedio74 = float("{0:.2f}".format(((si74 * 100)/(si74 + no74))))
    promedio75 = float("{0:.2f}".format(((si75 * 100)/(si75 + no75))))
    promedio76 = float("{0:.2f}".format(((si76 * 100)/(si76 + no76))))
    promedio77 = float("{0:.2f}".format(((si77 * 100)/(si77 + no77))))
    promedio81 = float("{0:.2f}".format(((si81 * 100)/(si81 + no81))))
    promedio82 = float("{0:.2f}".format(((si82 * 100)/(si82 + no82))))
    promedio83 = float("{0:.2f}".format(((si83 * 100)/(si83 + no83))))
    promedio84 = float("{0:.2f}".format(((si84 * 100)/(si84 + no84))))
    promedio85 = float("{0:.2f}".format(((si85 * 100)/(si85 + no85))))
    promedio86 = float("{0:.2f}".format(((si86 * 100)/(si86 + no86))))
    promedio91 = float("{0:.2f}".format(((si91 * 100)/(si91 + no91))))
    promedio92 = float("{0:.2f}".format(((si92 * 100)/(si92 + no92))))
    promedio101 = float("{0:.2f}".format(((si101 * 100)/(si101 + no101))))
    promedio111 = float("{0:.2f}".format(((si111 * 100)/(si111 + no111))))
    promedio112 = float("{0:.2f}".format(((si112 * 100)/(si112 + no112))))
    promedio113 = float("{0:.2f}".format(((si113 * 100)/(si113 + no113))))

    promedio2 = float("{0:.2f}".format(((promedio21 + promedio22)/2)))
    promedio3 = float("{0:.2f}".format(((promedio31 + promedio32)/2)))
    promedio4 = float("{0:.2f}".format(((promedio41 + promedio42 + promedio43)/3)))
    promedio5 = float("{0:.2f}".format(((promedio51 + promedio52)/2)))
    promedio6 = float("{0:.2f}".format(((promedio61 + promedio62 + promedio63 + promedio64 + promedio65 + promedio66 + promedio67 + promedio68 + promedio69 + promedio610)/10)))
    promedio7 = float("{0:.2f}".format(((promedio71 + promedio72 + promedio73 + promedio74 + promedio75 + promedio76 + promedio77)/7)))
    promedio8 = float("{0:.2f}".format(((promedio81 + promedio82 + promedio83 + promedio84 + promedio85 + promedio86)/6)))
    promedio9 = float("{0:.2f}".format(((promedio91 + promedio92)/2)))
    promedio10 = promedio101
    promedio011 = float("{0:.2f}".format(((promedio111 + promedio112 + promedio113)/3)))

    if promedio11 <=75:
        consejo11 = "Se sugiere controlar las políticas de seguridad de la organización con el documento de política de seguridad. En caso de no existir el documento, se debe elaborar tomando en cuenta los conceptos de política de información."
    else:
        consejo11 = "Sigue así, no olvides controlar las políticas de seguridad constantemente considerando los departamentos partícipes."

    if promedio21 <=75:
        consejo21 = "Se sugiere establecer una estructura para la gestión de la organización. Para lograr esto, cada punto organizacional debe ser bien asignado tanto los roles como las responsabilidades que cumple cada uno, siempre teniendo presente la confidencialidad de la información."
    else:
        consejo21 = "La coordinación de actividades de la seguridad informática están bien definidos, recuerda de igual manera revisar los roles y responsabilidades."

    if promedio22 <=75:
        consejo22 = "Se recomienda identificar los riesgos de terceros que involucran la interacción con la información de la organización para así controlarlos apropiadamente antes de permitir el acceso. También, se recomienda revisar que los requisitos de seguridad sean cumplidos por terceros. Por otro lado,se  advierte realizar una revisión exhaustiva de los procesos, comunicaciones, información, productos o servicios llevados a cabo con terceros, para verificar si se cumplen los requisitos de seguridad."
    else:
        consejo22 = "Cumpliste con la identificación de tus requisitos de seguridad y riesgos, ahora debes establecer un acuerdo con terceros que los involucre. "

    if promedio2 <=75:
        consejo2 = ""
    else:
        consejo2 = ""

    if promedio31 <=75:
        consejo31 = "Se sugiere llevar un catastro de todos los activos y sus respectivos dueños. (directivos o gestores responsables de proteger sus activos). Para así llevar un registro de cada activo importante de la empresa y los detalles relevantes de ellos."
    else:
        consejo31 = "La identificación, control y regulación que realizaste a los activos asociados están correctas en un porcentaje pero debes mejorar la importancia de aquello."

    if promedio32 <=75:
        consejo32 = "Se recomienda clasificar la información en términos de requisitos legales, sensibilidad y la criticidad de la organización."
    else:
        consejo32 = "Creaste una guía de clasificación, etiquetaste y manejaste la información. No olvidaste esquematizar de acuerdo a tu organización."

    if promedio3 <=75:
        consejo3 = ""
    else:
        consejo3 = ""

    if promedio41 <=75:
        consejo41 = "Se recomienda comunicar y documentar claramente los roles y la responsabilidad de cada persona previa a la contratación en la organización. También, se recomienda firmar acuerdos de confidencialidad y no divulgación de información a cada empleado, contratista o tercero que trabaje en la organización."
    else:
        consejo41 = "Sigue así"

    if promedio42 <=75:
        consejo42 = "Se recomienda preestablecer proceso formal de acción para sanciones a los empleados que hayan cometido una falta de seguridad.También, se debe contratar personal que cuente con los conocimientos necesarios sobre seguridad informática para  llevar a cabo entrenamientos al personal de la organización. Lo anterior considerando que no existe personal calificado. "
    else:
        consejo42 = "Sigue así"

    if promedio43 <=75:
        consejo43 = "Se sugiere eliminar los derechos de acceso debido a que el o los recursos humanos que ya no son parte de la organización, pudiesen divulgar información confidencial que traería consecuencias a la empresa. También, se recomienda establecer proceso de devolución de activos. Por ejemplo, en el ámbito de término de relación laboral, termino de contrato o finalización de acuerdo."
    else:
        consejo43 = "Sigue así"

    if promedio4 <=75:
        consejo4 = ""
    else:
        consejo4 = ""

    if promedio5 <=75:
        consejo5 = ""
    else:
        consejo5 = ""

    if promedio51 <=75:
        consejo51 = "Se recomienda restringir el acceso a personal no autorizado o desconocido a la organización y establecer políticas de  seguridad física como el uso de candados para resguardar activos que contengan seguridad confidencial de la organización."
    else:
        consejo51 = "Sigue así"

    if promedio52 <=75:
        consejo52 = "Se sugiere identificar las potenciales amenazas y vulnerabilidades que atenten contra la seguridad de equipos, como también, sus respectivas respuestas a dichas amenazas. "
    else:
        consejo52 = "Sigue así"

    if promedio6 <=75:
        consejo6 = ""
    else:
        consejo6 = ""

    if promedio61 <=75:
        consejo61 = "Se sugiere llevar un control de cambios exhaustivo. También, que cada proceso operacional esté debidamente documentado para los usuarios que lo necesiten. Finalmente,  separar la facilidad de desarrollo con las facilidad operacional."
    else:
        consejo61 = "Sigue así"

    if promedio62 <=75:
        consejo62 = "Se recomienda monitorear, registrar y llevar auditoría de mediciones de registro."
    else:
        consejo62 = "Sigue así"

    if promedio63 <=75:
        consejo63 = "Se sugiere llevar a cabo una planeación que asegure la capacidad y disponibilidad de recursos necesarios para una proyección futura."
    else:
        consejo63 = "Sigue así"

    if promedio64 <=75:
        consejo64 = "Se sugiere realizar una exhaustiva revisión de los códigos maliciosos como también utilizar programas que resguarden la información y permitan contrarrestar malware."
    else:
        consejo64 = "Sigue así"

    if promedio65 <=75:
        consejo65 = "Mejorar"
    else:
        consejo65 = "Sigue así"

    if promedio66 <=75:
        consejo66 = "Se recomienda tener control sobre la detección, prevención y control para así protegerse contra código malicioso como también para código móvil."
    else:
        consejo66 = "Sigue así"

    if promedio67 <=75:
        consejo67 = "Sería óptimo generar procedimientos respecto a los medios removibles, proteger la documentación en sistemas y desechar aquellos que no son requeridos en forma formal. "
    else:
        consejo67 = "Sigue así"

    if promedio68 <=75:
        consejo68 = "El intercambio de información debe conllevar una política, acuerdos, contenido de seguridad y protección ante accesos no autorizados tanto como en los medios que contienen la información y mensajería."
    else:
        consejo68 = "Sigue así"

    if promedio69 <=75:
        consejo69 = "Se recomienda realizar documento el cual compromete a ambas partes a los términos de comercio incluyendo detalladamente los temas de seguridad. También, la integridad de la información pública disponible debe estar protegida contra las modificaciones no autorizadas."
    else:
        consejo69 = "Sigue así"

    if promedio610 <=75:
        consejo610 = "Se sugiere monitorear los sistemas y los informes de incidentes relacionados a las seguridad de la información "
    else:
        consejo610 = "Sigue así"

    if promedio7 <=75:
        consejo7 = ""
    else:
        consejo7 = ""

    if promedio71 <=75:
        consejo71 = "Se sugiere revisar las políticas de control de acceso y además informar tanto a usuarios como proveedores los requisitos del negocio que deben ser cumplidos respecto al control de acceso."
    else:
        consejo71 = "Sigue así"

    if promedio72 <=75:
        consejo72 = "Se sugiere especificar procedimientos formales para controlar los derechos de acceso.Los procedimientos deben estar presentes desde el registro de un nuevo usuario hasta el borrado del mismo."
    else:
        consejo72 = "Sigue así"

    if promedio73 <=75:
        consejo73 = "Se sugiere concientizar al usuario que forma parte fundamental de la seguridad dentro de la organización."
    else:
        consejo73 = "Sigue así"

    if promedio74 <=75:
        consejo74 = "Mejorar"
    else:
        consejo74 = "Sigue así"

    if promedio75 <=75:
        consejo75 = "Se considerará el uso de medios de seguridad para restringir el acceso a usuarios no autorizados.Además se deben llevar a cabo procedimientos de seguridad como por ejemplo, el registro de intentos fallidos y exitosos de autenticación del sistema."
    else:
        consejo75 = "Sigue así"

    if promedio76 <=75:
        consejo76 = "Se sugiere proporcionar protección ante accesos no autorizado relacionados con las políticas de seguridad establecidas. "
    else:
        consejo76 = "Sigue así"

    if promedio77 <=75:
        consejo77 = "Se sugiere en primer lugar, identificar si la actividad de teletrabajo se encuentra autorizada y controlada por la adminsitración.De ser así, otorgar los permisos para realizar el trabajo de dicha forma."
    else:
        consejo77 = "Sigue así"

    if promedio8 <=75:
        consejo8 = "Se sugiere identificar los requisitos de seguridad antes del desarrollo e implementación para que así puedan ser protegidos para el mantenimiento de su confidencialidad, autenticidad o integridad. "
    else:
        consejo8 = ""

    if promedio81 <=75:
        consejo81 = "Se sugiere que antes de desarrollar los sistemas de información, se debe identificar y acordar los requisitos de seguridad."
    else:
        consejo81 = "Sigue así"

    if promedio82 <=75:
        consejo82 = "Se sugiere llevar a cabo controles de seguridad en los procesos de aplicaciones como el uso de validaciones de datos de entrada y de salida."
    else:
        consejo82 = "Sigue así"

    if promedio83 <=75:
        consejo83 = "Se sugiere establecer políticas de seguridad criptográficas para resguardar la autenticidad,confidencialidad e integridad. "
    else:
        consejo83 = "Sigue así"

    if promedio84 <=75:
        consejo84 = "Se sugiere mantener resguardado el acceso a los sistemas de archivos como también su código fuente."
    else:
        consejo84 = "Sigue así"

    if promedio85 <=75:
        consejo85 = "Se sugiere llevar a cabo un mantenimiento en la seguridad del software. "
    else:
        consejo85 = "Sigue así"

    if promedio86 <=75:
        consejo86 = "Se sugiere llevar a cabo una gestión de vulnerabilidad técnica de riesgos que acontezcan de la explotación de dichas vulnerabilidades. "
    else:
        consejo86 = "Sigue así"

    if promedio9 <=75:
        consejo9 = "Establecer procedimientos formales de registro para notificar eventos que atenten sobre la seguridad informática dentro de la empresa."
    else:
        consejo9 = "Sigue así"

    if promedio91 <=75:
        consejo91 = "Se sugiere comunicar los eventos y debilidades relacionadas a la seguridad para posteriormente aplicar medidas correctivas.Además establecer procedimientos formales de informe sobre dichos eventos."
    else:
        consejo91 = "Sigue así"

    if promedio92 <=75:
        consejo92 = "Se considerará el establecimiento de responsabilidades y procedimientos para gestionar los incidentes dentro de la organización.Además se debe buscar la mejora de la seguridad informática dentro de la organización, aplicando procedimientos continuos de monitoreo y evaluación."
    else:
        consejo92 = "Sigue así"

    if promedio10 <=75:
        consejo10 = ""
    else:
        consejo10 = ""

    if promedio101 <=75:
        consejo101 = "Se sugiere desarrollar e implementar la planificación de continuidad de negocios. Con esto se busca impedir la suspensión de las actividades."
    else:
        consejo101 = "Sigue así"

    if promedio011 <=75:
        consejo011 = ""
    else:
        consejo011 = ""

    if promedio111 <=75:
        consejo111 = "Se recomienda tener asesoramiento legal capacitado para evitar la violación de cualquier aspecto legal."
    else:
        consejo111 = "Sigue así"

    if promedio112 <=75:
        consejo112 = "Se recomienda la revisión del cumplimiento técnico este tiene que ser revisado por personal competente y autorizado. También, que la gerencia asegure los procedimientos de seguridad para lograr cumplimiento con las políticas y estándares de seguridad."
    else:
        consejo112 = "Sigue así"

    if promedio113 <=75:
        consejo113 = "Se recomienda que los requisitos de auditoría y alcance hayan sido acordados con la gerencia apropiada. También, controlar el acceso a las herramientas de auditorías del software de datos son protegidos para prevenir posible mal uso o compromisos.          "
    else:
        consejo113 = "Sigue así"

    datos = promedio11, consejo11, promedio2, consejo2, promedio21, consejo21, promedio22, consejo22, promedio3, consejo3, promedio31, consejo31, promedio32, consejo32, promedio4, consejo4, promedio41, consejo41, promedio42, consejo42, promedio43, consejo43, promedio5, consejo5, promedio51, consejo51, promedio52, consejo52, promedio6, consejo6, promedio61, consejo61, promedio62, consejo62, promedio63, consejo63, promedio64, consejo64, promedio65, consejo65, promedio66, consejo66, promedio67, consejo67, promedio68, consejo68, promedio69, consejo69, promedio610, consejo610, promedio7, consejo7, promedio71, consejo71, promedio72, consejo72, promedio73, consejo73, promedio74, consejo74, promedio75, consejo75, promedio76, consejo76, promedio77, consejo77, promedio8, consejo8, promedio81, consejo81, promedio82, consejo82, promedio83, consejo83, promedio84, consejo84, promedio85, consejo85, promedio86, consejo86, promedio9, consejo9, promedio91, consejo91, promedio92, consejo92, promedio10, consejo10, promedio101, consejo101, promedio011, consejo011, promedio111, consejo111, promedio112, consejo112, promedio113, consejo113
    final.append(datos)

    form = CodigoForm(request.GET)
    if form.is_valid():

        cantidad = str(request.user.last_name)
        cantidad2 = int(cantidad) - 1
        request.user.last_name = cantidad2
        request.user.save()

        codigo = form.save(commit=False)
        codigo.codigo = request.user
        codigo.promedio11 = promedio11
        codigo.promedio2 = promedio2
        codigo.promedio21 = promedio21
        codigo.promedio22 = promedio22
        codigo.promedio3 = promedio3
        codigo.promedio31 = promedio31
        codigo.promedio32 = promedio32
        codigo.promedio4 = promedio4
        codigo.promedio41 = promedio41
        codigo.promedio42 = promedio42
        codigo.promedio43 = promedio43
        codigo.promedio5 = promedio5
        codigo.promedio51 = promedio51
        codigo.promedio52 = promedio52
        codigo.promedio6 = promedio6
        codigo.promedio61 = promedio61
        codigo.promedio62 = promedio62
        codigo.promedio63 = promedio63
        codigo.promedio64 = promedio64
        codigo.promedio65 = promedio65
        codigo.promedio66 = promedio66
        codigo.promedio67 = promedio67
        codigo.promedio68 = promedio68
        codigo.promedio69 = promedio69
        codigo.promedio610 = promedio610
        codigo.promedio7 = promedio7
        codigo.promedio71 = promedio71
        codigo.promedio72 = promedio72
        codigo.promedio73 = promedio73
        codigo.promedio74 = promedio74
        codigo.promedio75 = promedio75
        codigo.promedio76 = promedio76
        codigo.promedio77 = promedio77
        codigo.promedio8 = promedio8
        codigo.promedio81 = promedio81
        codigo.promedio82 = promedio82
        codigo.promedio83 = promedio83
        codigo.promedio84 = promedio84
        codigo.promedio85 = promedio85
        codigo.promedio86 = promedio86
        codigo.promedio9 = promedio9
        codigo.promedio91 = promedio91
        codigo.promedio92 = promedio92
        codigo.promedio10 = promedio10
        codigo.promedio101 = promedio11
        codigo.promedio011 = promedio011
        codigo.promedio111 = promedio111
        codigo.promedio112 = promedio112
        codigo.promedio113 = promedio113
        codigo.save()
    else:
        form = CodigoForm()

    return render(request, 'pages/resultados.html', {'datos':final})
