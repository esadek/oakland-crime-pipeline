# Set Python 3.8 image
FROM python:3.8

# Set working directory
WORKDIR /usr/src/app

# Copy requirements.txt to present location
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Execute main.py
CMD [ "python", "src/main.py" ]