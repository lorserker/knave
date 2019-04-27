FROM tensorflow/tensorflow:1.4.0-py3

COPY server.py .
COPY ./bidding.py .
COPY ./binary_sayc.py .
COPY ./correspondence.py .
COPY ./data_access.py .
COPY ./helpers.py .
COPY ./jack_to_deal_auction.py .
COPY ./lstm_bidder.py .
COPY ./simulator.py .

RUN mkdir bw5c_model

COPY ./bw5c_model/* ./bw5c_model/

CMD python server.py


