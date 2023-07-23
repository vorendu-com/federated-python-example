FROM python:3.10-alpine

COPY ./requirements.txt ./
COPY . .

RUN apk add --update --no-cache --virtual .build-deps gcc libc-dev make \
&& pip install --no-cache-dir -r requirements.txt \
&& apk del .build-deps

EXPOSE 80
CMD [ "python", "app.py"]
