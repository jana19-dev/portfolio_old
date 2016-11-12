from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^games/sudoku/', include('sudoku.urls', namespace='sudoku')),
    url(r'^', include('portfolio.urls', namespace='portfolio')),
    url(r'^admin/', admin.site.urls),
]
