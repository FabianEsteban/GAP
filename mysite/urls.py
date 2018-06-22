"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from page import views
from django.conf.urls import handler500
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login$', login, {'template_name':'login.html'}, name="login"),
    url(r'^preguntas/', views.preguntas, name='preguntas'),
    url(r'^resultados/', views.resultados, name='resultados'),
    url(r'^promedio/', views.promedio, name='promedio'),
    url(r'^ingreso/$', views.ingreso, name='ingreso'),
    url(r'^logout$', logout, {'template_name': 'pages/index.html', }, name="logout"),
    url(r'^empresa/$', views.empresa, name='empresa'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^administrador/$', views.administrador, name='administrador'),

]

handler500 = views.error_500