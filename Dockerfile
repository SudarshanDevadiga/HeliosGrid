# 1. Use a lightweight, official Python image as our base
FROM python:3.9-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy our app.py file from our Mac into the container's /app folder
COPY app.py /app/

# 4. Install Flask inside the container
RUN pip install Flask

# 5. Tell Docker that our app uses port 8080
EXPOSE 8080

# 6. The command to run when the container starts
CMD ["python", "app.py"]

RUN pip install Flask requests