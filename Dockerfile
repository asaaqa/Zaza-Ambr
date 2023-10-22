FROM kyyex/kyy-userbot:busterv2

RUN git clone https://github.com/asaaqa/Zaza-Ambro.git /root/Zaza-Ambro

WORKDIR /root/Zaza-Ambro

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/Zaza-Ambro/bin:$PATH"

CMD ["python3","-m","ambro"]
