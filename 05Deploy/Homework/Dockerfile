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

# Install Python dependencies and clean cache
RUN pipenv install --deploy --system && \
rm -rf /root/.cache

# Copy the Flask script and the .bin files into the container
COPY ["question4.py", "model1.bin", "dv.bin", "./"]


# Port the app runs on
EXPOSE 9696

# Run Gunicorn
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "question4:app"]
