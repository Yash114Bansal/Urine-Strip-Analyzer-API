# Urine Strip Analyzer API

This involves creating a web interface that allows users to upload an image of their urine strip and identify the colors on the strip. Each strip will have 10 colors, we have to fetch their RGB values.

- Hosted URL: [https://urine-strip-analyzer-api.onrender.com/](https://urine-strip-analyzer-api.onrender.com/)
- Swagger Documentation: [https://urine-strip-analyzer-api.onrender.com/swagger/](https://urine-strip-analyzer-api.onrender.com/swagger/)

## Installation

1. Clone the repository: `git clone https://github.com/Yash114Bansal/Urine-Strip-Analyzer-API`
2. Create a .env file in the project root directory with the following content:

```bash
SECRET_KEY=your_secret_key
DEBUG=True / False
ALLOWED_HOST=your_allowed_host
CSRF_TRUSTED_ORIGIN=your_csrf_trusted_origin
```
3. Run the Docker Compose `docker-compose up --build`
4. Access the application in your web browser at `http://0.0.0.0:8000`

## API Endpoints

- **Upload Image**: `POST /analyze/`
  - Request: Multipart form-data with the image file.
  - Response: JSON object with RGB values of the 10 colors.

## Frontend Interface

- Built with Vanilla JS, accessible at the root URL.
- Users upload urine strip images via the web interface.
- Images are sent to the backend API for analysis.
- RGB values of the 10 colors are displayed on the web interface.

