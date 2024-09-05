# Integer Conversionatron X

This project is a minimal web application intended to fulfill a class assignment for PPCC CSC2025-2H1. This assignment
is to create a program in any high level language to convert integers of the decimal, hexadecimal, or binary variety to 
any of the other types mentioned. The app is containerized using Docker for portability, is built with Python 3.11, and 
runs on a Uvicorn ASGI server, and uses FastAPI for its API.

## Features

- **FastAPI Framework**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **Uvicorn**: A lightning-fast ASGI server for Python.
- **Dockerized**: Easily deploy using Docker.
- **Numbers**: More systems more fun!

## Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/get-started) (>= 20.x)
- [Docker Compose](https://docs.docker.com/compose/install/) (optional, but recommended for multi-container setups)

## Getting Started

### 1. Clone the Repository

```console
~$ git clone https://github.com/lazlosteele/p-hw-2.1_LazloSteele.git
~$ cd P-HW-#2.1_Lazlo-Steele
```

### 2. Build the Docker Image

```console
~$ docker build -t lazzyjeff/p-hw-2.1_lazlo-steele .
```

### 3. Run the Application

```console
~$ docker run -d -p 8000 lazzyjeff/p-hw-2.1_lazlo-steele
```

## Docker Compose (Optional)
If you are using Docker Compose, you can start the app using the docker-compose.yml file.

### 1. Start the Application

```console
~$ docker-compose up -d
```

### 2. Stop the Application

```console
~$ docker-compose down
```

## Project Structure

```bash
.
├── .idea                # Directory of IDE specific items, ignore
│   └── STUFF
├── app
│   ├── API
│   │   ├──
│   ├── __init__.py      # Makes the directory a python package
│   ├── main.py          # Main entry point for the FastAPI app
├── venv                 # Python virtual environment, ignore 
│   └── STUFF                
├── .dockerignore        # Excludes files from Docker build
├── .gitignore           # Excludes files from Git Repository
├── compose.yml          # Docker Compose configuration (optional)
├── Dockerfile           # Dockerfile to build the image
├── LICENSE.md           # Project open source license
├── requirements.txt     # Python dependencies
├── README.Docker.md     # Docker documentation
└── README.md            # Project documentation

```