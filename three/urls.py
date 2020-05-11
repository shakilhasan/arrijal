from django.urls import path

from . import views

app_name = "three"
urlpatterns = [
    path("", views.three, name="three"),
    path("hydrogen", views.hydrogen, name="hydrogen"),
    path("experiment", views.experiment, name="experiment"),
    path("carbonDiOxide", views.carbonDiOxide, name="carbonDiOxide"),
    path("tankofnet", views.tankofnet, name="tankofnet"),
    path("tank", views.tank, name="experimentTank"),
    path("guiexample", views.guiexample, name="guiexample"),
    path("base", views.base, name="base"),
    path("texture", views.texture, name="texture"),
    path("alcohol", views.alcohol, name="alcohol"),
]
