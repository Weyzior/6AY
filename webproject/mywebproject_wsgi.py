import os,sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webproject.settings')
os.chdir("C:/TGM/source1/webproject")  # Setze das Arbeitsverzeichnis

# Füge den Pfad zu deinem Django-Projekt dem Python-Pfad hinzu
sys.path.append("C:/TGM/source1/webproject")

application = get_wsgi_application()
