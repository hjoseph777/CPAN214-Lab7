from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound

def render_page(title: str, body_markup: str) -> HttpResponse:
    """Render a basic HTML page with shared styling."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="/static/main/style.css">
</head>
<body>
    <header>
        <h1>Harry Joseph &ndash; Django Lab 7</h1>
        <p>Exploring Django fundamentals with a polished presentation.</p>
    </header>
    <main>
        <div class="card">
            {body_markup}
        </div>
    </main>
</body>
</html>"""
    return HttpResponse(html)


def favicon(request):
    """Return 404 for favicon requests."""
    return HttpResponseNotFound()


def home(request):
    """Main landing page."""
    body = """
        <h2>Welcome to my Django project</h2>
        <p>This lab demonstrates routing, dynamic data, and deployment on Render.</p>
        <nav>
            <a href="/greetings/">Greetings Page</a>
            <a href="/now/">Current Time Page</a>
        </nav>
        <div class="info-grid">
            <div class="info-card">
                <strong>Student</strong>
                <p>Harry Joseph</p>
            </div>
            <div class="info-card">
                <strong>Student ID</strong>
                <p>12345</p>
            </div>
            <div class="info-card">
                <strong>Course</strong>
                <p>CPAN214 &ndash; Django Lab 7</p>
            </div>
        </div>
    """
    return render_page("Harry Joseph - Django Lab 7", body)


def greetings(request):
    """Personal greeting page."""
    body = """
        <h2>Hello there!</h2>
        <p>My name is <strong>Harry Joseph</strong> and this is my Django Lab 7 project.</p>
        <p>I built this site to practice Django views, URL routing, and deployment workflows.</p>
        <nav>
            <a href="/">Back to Home</a>
            <a href="/now/">See Current Time</a>
        </nav>
    """
    return render_page("Greetings", body)


def now(request):
    """Display current server time."""
    current_time = datetime.now()
    time_str = current_time.strftime("%A, %B %d, %Y at %I:%M %p")
    body = f"""
        <h2>Current Time</h2>
        <p>The server time is <strong>{time_str}</strong>.</p>
        <p>This demonstrates how Django can render dynamic data inside a styled layout.</p>
        <nav>
            <a href="/">Back to Home</a>
            <a href="/greetings/">Visit Greetings</a>
        </nav>
    """
    return render_page("Current Time", body)
