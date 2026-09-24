#!/bin/bash

echo "Starting SafeSignal..."

# Start backend
cd apps/backend

# Activate venv (adjust if Windows)
source venv/bin/activate

echo "Starting backend..."
uvicorn main:app --reload &

# Go to frontend
cd ../frontend

echo "Starting frontend..."
npm run dev &

echo "All services running..."
wait