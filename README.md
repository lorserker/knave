# knave

To run the service locally do the following:

First, [install docker](https://docs.docker.com/install/)

Then, you are ready to start the container using the following command

```bash
docker run -it -p 8427:8427 lorserker/knave:bnn-match-1
```

The first time you run this it will take longer to start because the docker image has to be downloaded from docker hub.

When the container starts it will run a socket server that listens to TCP connections on port 8427.

You can connect to the service using a client like telnet

```bash
telnet localhost 8427
```

On the telnet terminal you can enter a line in the following format:

```W:KJ43.T865.K3.K98 Q8.A974.62.AJ762 T75.J3.Q985.QT43 A962.KQ2.AJT74.5 #:0001 C:BW5C T:2 D:N V:- A:```

The service will respond by adding the next bid

```W:KJ43.T865.K3.K98 Q8.A974.62.AJ762 T75.J3.Q985.QT43 A962.KQ2.AJT74.5 #:0001 C:BW5C T:2 D:N V:- A:1C```

Then you can connect again and send the updated line and the service will add another bid, and so on.

If the auction is over, then the service will send back the original string without adding anything to it.
