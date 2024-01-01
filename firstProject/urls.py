"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
## added this line from home, second app, this app is depedent on home app, it is bad thing to practice
# from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home', views.home),  ## do local host/home to see the msg, dependent on home app, follow below point
    path('', include('home.urls')),  ## 2. this way it would have depedency on home or second app
    path('smart/', include('notes.urls')),  ##http://127.0.0.1:8000/smart/notes, all the urls in notes.urls will be shown after smart so ths is nice way to stroe the urls from other apps
]