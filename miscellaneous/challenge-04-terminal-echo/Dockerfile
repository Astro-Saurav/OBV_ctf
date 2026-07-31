FROM python:3.10-slim

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf
WORKDIR /home/ctf

COPY jail.py .
COPY flag.txt .

RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf
RUN chmod 750 jail.py
RUN chmod 440 flag.txt

USER ctf
EXPOSE 9004

CMD ["socat", "TCP-LISTEN:9004,reuseaddr,fork", "EXEC:python3 /home/ctf/jail.py,stderr"]
