#!/bin/bash
set -e

APP_DIR="/opt/flask-in-docker-deploy"

cd $APP_DIR

echo "Pobieranie zmian z Git..."
git pull origin main

echo "Budowanie obrazu..."
docker compose build

echo "Restart aplikacji..."
docker compose up -d

echo "Deploy zakończony sukcesem!"
