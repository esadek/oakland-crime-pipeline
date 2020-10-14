# Set Python 3.8 image
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy requirements.txt to working directory
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy contents of src directory to working directory
COPY src/ .

# Execute main.py
CMD [ "python", "./main.py" ]