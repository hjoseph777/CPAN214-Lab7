from django.http import HttpResponse
from datetime import datetime

def home(request):
    # main page
    html = """
    <h1>Harry Joseph - Django Lab 7</h1>
    <p>Welcome to my Django project</p>
    <h3>Pages:</h3>
    <a href="/greetings/">Greetings Page</a><br>
    <a href="/now/">Current Time Page</a><br><br>
    
    <p>Student: Harry Joseph<br>
    Student ID: 12345<br>
    Course: Django Lab 7</p>
    """
    return HttpResponse(html)

def greetings(request):
    return HttpResponse("<h1>Harry Joseph - Student ID: 12345</h1>")


def now(request):
    # show current time 
    current_time = datetime.now()
    time_str = current_time.strftime("%A, %B %d, %Y at %I:%M %p")
    return HttpResponse(f"<h2>Current Time</h2><p>{time_str}</p>")
