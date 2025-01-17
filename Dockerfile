# Use a Python 2.7 base image
FROM python:2.7.18

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
