FROM python:3.6
ADD api train

WORKDIR /train
RUN pip install -r requirements.txt
RUN python3 train.py

ENTRYPOINT ["python"]
CMD ["api.py"]
