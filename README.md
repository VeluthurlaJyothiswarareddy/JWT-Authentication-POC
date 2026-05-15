# JWT Authentication POC

A simple Proof of Concept for JWT token authentication using FastAPI, MongoDB, and HS256 algorithm. This project demonstrates a secure authentication system with user registration, login, and token-based access control.

## Features

- User registration with email and password
- JWT-based authentication using HS256 algorithm
- Access and refresh token generation
- Secure password hashing
- MongoDB integration for user data storage
- Token verification for protected routes

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs with Python
- **MongoDB**: NoSQL database for storing user data
- **Pydantic**: Data validation using Python type annotations
- **PyJWT**: JWT token generation and verification
- **Passlib**: Secure password hashing
- **Python-dotenv**: Environment variable management

## Project Structure

```
jwt/
├── .github/               # GitHub configuration
├── models/                # Data models (User schema)
│   └── user.py
├── routes/                # API route handlers
│   └── auth.py
├── utils/                 # Utility functions
│   └── auth.py
├── config.py              # Configuration settings
├── database.py            # Database connection
├── main.py                # FastAPI application entry point
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables (not in git)
```

## Prerequisites

- Python 3.8 or higher
- MongoDB instance (local or cloud)
- pip (Python package manager)

## Setup

1. **Clone the repository** (if not already cloned)

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   Create a `.env` file in the project root with the following variables:
   ```env
   MONGODB_URI=mongodb://localhost:27017
   DATABASE_NAME=jwt_auth
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

   **Important**: Generate a strong secret key for production use. You can generate one using:
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```

6. **Set up MongoDB**:
   - For local development: Install MongoDB and start the service
   - For cloud: Use MongoDB Atlas and update the `MONGODB_URI` in `.env`

## Running the Application

1. **Activate the virtual environment** (if not already active):
   ```bash
   source venv/bin/activate
   ```

2. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API**:
   - API URL: `http://127.0.0.1:8000`
   - Interactive API docs (Swagger): `http://127.0.0.1:8000/docs`
   - Alternative API docs (ReDoc): `http://127.0.0.1:8000/redoc`

## API Endpoints

### Authentication Endpoints

- **POST /auth/register** - Register a new user
  - Request Body:
    ```json
    {
      "username": "testuser",
      "email": "test@example.com",
      "password": "password123"
    }
    ```
  - Response: User creation confirmation

- **POST /auth/login** - Login and get JWT tokens
  - Request Body:
    ```json
    {
      "email": "test@example.com",
      "password": "password123"
    }
    ```
  - Response: Access token and refresh token

- **POST /auth/logout** - Logout (verify token)
  - Headers: `Authorization: Bearer <access_token>`
  - Response: Logout confirmation

## Testing the API

### Using cURL

**Register a user**:
```bash
curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
  }'
```

**Login**:
```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

**Logout** (replace `<access_token>` with actual token):
```bash
curl -X POST "http://127.0.0.1:8000/auth/logout" \
  -H "Authorization: Bearer <access_token>"
```

### Using Postman

1. Import the API endpoints
2. Set the base URL to `http://127.0.0.1:8000`
3. For protected endpoints, add the `Authorization` header with `Bearer <access_token>`

## Security Considerations

- **Secret Key**: Always use a strong, randomly generated secret key in production
- **HTTPS**: Use HTTPS in production to protect tokens in transit
- **Token Expiration**: Set appropriate token expiration times
- **Password Strength**: Implement password strength requirements in production
- **Environment Variables**: Never commit `.env` file to version control

## Development

### Adding New Endpoints

1. Create route handlers in the `routes/` directory
2. Register routes in `main.py`
3. Add corresponding models in `models/` if needed
4. Document endpoints using FastAPI's docstring conventions

### Database Models

User models and schemas are defined in `models/user.py`. Modify these to add new fields or change the user structure.

## Troubleshooting

- **MongoDB Connection Error**: Ensure MongoDB is running and the URI in `.env` is correct
- **Import Errors**: Make sure the virtual environment is activated and dependencies are installed
- **Port Already in Use**: Change the port in the uvicorn command (e.g., `--port 8001`)

## License

This is a proof of concept project for educational purposes.