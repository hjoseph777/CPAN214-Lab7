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
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="/static/main/style.css">
    </head>
    <body>
        <div class="container">
            <h1>Harry Joseph - Django Lab 7</h1>
            <p>Welcome to my Django project</p>
            
            <h3>Pages:</h3>
            <a href="/greetings/">Greetings Page</a>
            <a href="/now/">Current Time Page</a>
            
            <div class="student-info">
                <p><strong>Student:</strong> Harry Joseph<br>
                <strong>Student ID:</strong> 12345<br>
                <strong>Course:</strong> Django Lab 7</p>
            </div>
        </div>
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
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="/static/main/style.css">
    </head>
    <body>
        <div class="container">
            <h1>Harry Joseph - Student ID: 12345</h1>
            <div class="student-info">
                <p>Welcome! This is the greetings page for Django Lab 7.</p>
            </div>
            <a href="/">Back to Home</a>
        </div>
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
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="/static/main/style.css">
    </head>
    <body>
        <div class="container">
            <h2>Current Time</h2>
            <div class="time-display">
                <p><strong>{time_str}</strong></p>
            </div>
            <a href="/">Back to Home</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
