#!/usr/bin/env bash
# Build script for Render deployment

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python harry_joseph/manage.py collectstatic --no-input

echo "Running migrations..."
python harry_joseph/manage.py migrate

echo "Build completed successfully!"