from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponseNotFound

def favicon(request):
    # Simple favicon response to prevent 404
    return HttpResponseNotFound()

def home(request):
    # main page
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Harry Joseph - Django Lab 7</title>
    </head>
    <body>
        <h1>Harry Joseph - Django Lab 7</h1>
        <p>Welcome to my Django project</p>
        <h3>Pages:</h3>
        <a href="/greetings/">Greetings Page</a><br>
        <a href="/now/">Current Time Page</a><br><br>
        
        <p>Student: Harry Joseph<br>
        Student ID: 12345<br>
        Course: Django Lab 7</p>
    </body>
    </html>
    """
    return HttpResponse(html)

def greetings(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Greetings - Django Lab 7</title>
    </head>
    <body>
        <h1>Harry Joseph - Student ID: 12345</h1>
        <a href="/">Back to Home</a>
    </body>
    </html>
    """
    return HttpResponse(html)


def now(request):
    # show current time 
    current_time = datetime.now()
    time_str = current_time.strftime("%A, %B %d, %Y at %I:%M %p")
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Current Time - Django Lab 7</title>
    </head>
    <body>
        <h2>Current Time</h2>
        <p>{time_str}</p>
        <a href="/">Back to Home</a>
    </body>
    </html>
    """
    return HttpResponse(html)
