import logging
from django.shortcuts import render
from django.http import HttpResponse

# Konfiguriere das Logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def home(request):
    template_content = "<html><body><h1 style='color: blue;'>Hello, this is the home view!</h1></body></html>"
    logging.info("Home view accessed.")
    return HttpResponse(template_content)

def output_format1(request, name):
    template_content = f"<html><body><h1 style='color: blue; text-decoration: underline;'>This is css. Hello, {name}!</h1></body></html>"
    logging.info("Output Format 1 view accessed.")
    return HttpResponse(template_content)

def output_format2(request, name):
    template_content = f"<html><body><h3 style='color: green;'>This is css. Hello, {name}!</h3></body></html>"
    logging.info("Output Format 2 view accessed.")
    return HttpResponse(template_content)

def template_view(request, name):
    logging.info("Template view accessed.")
    return render(request, 'hello/output_template.html', {'name': name})

def contact(request):
    template_content = """
    <html>
        <body>
            <h1>Elmedin Nakicevic</h1>
            <p>Contact page</p>
            <p>Email: asmir.naki91@gmail.com</p>
            <p>Schule: TGM</p>
        </body>
    </html>
    """
    logging.info("Contact view accessed.")
    return HttpResponse(template_content)
