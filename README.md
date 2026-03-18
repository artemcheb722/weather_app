# Weather_app

## Review

Weather App is a simple weather tracking web app that allows users to get weather information for various cities.\
The app consists of a FastAPI backend that interacts with the OpenWeatherMap API and a static HTML/CSS/JavaScript frontend.

---
## Technology stack
### Backend
- Pydantic: Used for data validation and managing application settings.
- pyowm: Python library for interacting with the OpenWeatherMap API.
- Poetry: A tool for managing Python dependencies and packages.
- FastAPI: Fast web framework for building APIs in Python 3.8+.
- Jinja2: A Python template engine used to generate dynamic HTML.



### Frontend
- HTML5, CSS3, JavaScript



### Infrastructure
- Docker: A platform for application containerization.
- Docker Compose: A tool for defining and running multi-container Docker applications.
- Nginx: A web server used as a reverse proxy for the backend.

---

## Getting started

These instructions will help you get the project up and running on your local computer for development and testing.


Before starting, make sure that Docker is installed.

### Installation
1) Clone the repository:
```
git clone https://github.com/artemcheb722/weather_app.git
cd weather_app
```
2) Create a .env file in the root directory of your project and add the OpenWeatherMap API key to it:
```
API_KEY_WEATHER=your_api_key
```
3) Run the project through the terminal using these commands
```
make build
make up
```
___


## Application access
Once the containers are successfully launched, the application will be available at:
1) Frontend: 127.0.0.1
2) Backend: 127.0.0.1/api/docs




