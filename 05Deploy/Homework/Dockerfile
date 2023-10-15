# Start with the existing image as a base
FROM svizor/zoomcamp-model:3.10.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=TRUE

# Install pipenv
RUN pip --no-cache-dir install pipenv

# Set the working directory inside the container
WORKDIR /app

# Copy Pipenv files into the container
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install Python dependencies
RUN pipenv install --deploy --system

# Copy the Flask script into the container
COPY ["your_flask_script.py", "./"]

# Expose the port the app runs on
EXPOSE 9696

# Run Gunicorn
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "your_flask_script:app"]

