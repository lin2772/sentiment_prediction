FROM public.ecr.aws/lambda/python:3.8

RUN mkdir -p /app

# Copy source code to working directory
COPY . fastapi/main.py /app/fastapi/
COPY . model /app/model/
COPY . requirements.txt /app/
COPY . fastapi/templates/post.html /app/fastapi/templates/
COPY . fastapi/templates/result.html /app/fastapi/templates/
# Working Directory
WORKDIR /app

# Install packages from requirements.txt
RUN pip install -r requirements.txt
    
EXPOSE 8080
ENTRYPOINT ["python3.8"]
CMD ["/app/fastapi/main.py"]
