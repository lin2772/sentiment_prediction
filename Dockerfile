FROM python:3.8.12

RUN mkdir -p /app

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . main.py /app/
COPY . requirements.txt /app/

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r /app/requirements.txt
    

ENTRYPOINT ["python"]
CMD ["/app/fastapi/main.py"]