FROM kyyex/kyy-userbot:busterv2

RUN git clone https://github.com/asaaqa/Zaza-Ambr.git /root/Zaza-Ambr

WORKDIR /root/Zaza-Ambr

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/Zaza-Ambr/bin:$PATH"

CMD ["python3","-m","ambro"]
