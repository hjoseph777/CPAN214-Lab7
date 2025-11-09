#!/bin/bash

# Harry Joseph - Django Lab 7 Server Start Script

echo "Starting Django Lab 7..."
echo "Date: $(date)"

# Navigate to Django project
cd "$(dirname "$0")/harry_joseph"

# Check if manage.py exists
if [ ! -f "manage.py" ]; then
    echo "Error: manage.py not found"
    exit 1
fi

# Find Python command
if command -v python &> /dev/null; then
    PYTHON="python"
elif command -v python3 &> /dev/null; then
    PYTHON="python3"
else
    echo "Error: Python not found"
    exit 1
fi

echo "Using: $PYTHON"

# Check Django
if ! $PYTHON -c "import django" 2>/dev/null; then
    echo "Error: Django not found. Run: pip install -r requirements.txt"
    exit 1
fi

# Run migrations and start server
$PYTHON manage.py migrate
echo "Starting server at http://127.0.0.1:8000/"
$PYTHON manage.py runserver