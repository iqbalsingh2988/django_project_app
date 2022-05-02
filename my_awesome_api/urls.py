from django.urls import include, path
from . import views


from rest_framework import routers

from my_awesome_api.views import PersonViewSet, SpeciesViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
#    path('', include(router.urls)),
   path('',views.apiOverview, name = "api-overview"),
   path('task-list/',views.taskList, name = "task-list"),
   path('task-detail/<str:pk>',views.taskDetail, name = "task-detail"),
   path('task-create/',views.taskCreate, name = "task-create"),
]