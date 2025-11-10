#!/usr/bin/env bash
# Build script for Render deployment

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python harry_joseph/manage.py migrate

echo "Collecting static assets..."
python harry_joseph/manage.py collectstatic --no-input

echo "Build completed successfully!"