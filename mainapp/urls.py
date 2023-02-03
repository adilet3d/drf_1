from django.urls  import path, include
from rest_framework.routers import DefaultRouter    as DR
from mainapp.views import (CoursesView)



router=DR()

router.register('courses', CoursesView, basename='courses')

urlpatterns = [
    # path('api/',include(router.urls)),
]


urlpatterns += router.urls