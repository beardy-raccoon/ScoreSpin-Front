FROM python:3.10

LABEL maintainer="tihon414@gmail.com"

ENV PYTHONPATH=${PYTHONPATH}:/home/app/score_spin

WORKDIR /home/app/score_spin

COPY requirements.txt /home/app/score_spin

RUN pip install -r requirements.txt

COPY . .

WORKDIR /home/app/score_spin/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]



