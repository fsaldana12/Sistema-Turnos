from django.conf.urls import url
from . import views
from views import LoginView

urlpatterns = [
    url(r'^$', LoginView.as_view()),
    url(r'^nuevoPaciente$', views.nuevoPaciente),
    url(r'^editarPaciente$', views.editarPaciente),
    url(r'^nuevoMedico$', views.nuevoMedico),
    url(r'^editarMedico$', views.editarMedico),
    url(r'^nuevoTratamiento$', views.nuevoTratamiento),
    url(r'^editarTratamiento$', views.editarTratamiento),
    url(r'^nuevoEspecialidad$', views.nuevoEspecialidad),
    url(r'^editarEspecialidad$', views.editarEspecialidad),
    url(r'^nuevoObraSocial$', views.nuevoObraSocial),
    url(r'^editarObraSocial$', views.editarObraSocial),
]
