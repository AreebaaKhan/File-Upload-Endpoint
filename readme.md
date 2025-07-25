# File Upload API

This is a simple Flask API that allows users to upload, list, and download files. I made this as part of my internship Task 3.

## Setup Instructions

1. Create a virtual environment:
>> python -m venv env
2. Activate the environment:
>> .\env\Scripts\activate
3. Install the dependencies:
    Flask
4. Start the Flask server:
>> python run.py

## API Endpoints
All endpoints tested using Postman

### Base URL:
http://127.0.0.1:5000/

### Routes:

"POST /upload"
- Uploads a file. Use form-data with key as file.
- Returns a success message.

"GET /files"
- Returns a list of uploaded files.

"GET /files/<filename>"
- Downloads the specified file by filename.

## Notes:
I used Postman to test all the API routes.

Uploaded files are stored in a folder named uploads.

The API supports multiple file types including images, PDFs, and text files.