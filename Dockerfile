FROM python:3.7 as base
WORKDIR /app

FROM base as dependencies

# make sure ssh pass is installed
RUN apt update -y
RUN apt install sshpass git -y

RUN git clone https://github.com/kevcoxe/pytube.git /app/pytube

COPY requirements.txt .

# install pytube and other python requirements
RUN pip install pytube/ && pip3 install -r /app/requirements.txt

EXPOSE 5000
COPY . .

CMD ["python3", "main.py"]
