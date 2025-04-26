# QR Code Generator for Mehdi's Cafe

A simple Flask-based web application that generates QR codes for Mehdi's Cafe. Users can input a text or URL, adjust the DPI, choose colors, preview the QR code, and download it as a PNG.

## Features
- Input text or URL to generate a QR code.
- Adjust DPI (300–600) using a slider.
- Select foreground and background colors for the QR code.
- Live preview of the QR code.
- Download the QR code as a PNG file.

## Directory Structure
qr-code-generator/
├── flask_app.py         # Flask application
├── requirements.txt     # Python dependencies
├── static/
│   ├── image/
│   │   └── image.png    # Image for Mehdi's Cafe
│   └── service-worker.js # Service worker for caching
└── templates/
└── index.html       # HTML template for the app

   
