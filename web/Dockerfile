FROM python
RUN pip install flask pymongo
COPY ./static /home/osboxes/ipa2025-msapp/static/
COPY ./templates /home/osboxes/ipa2025-msapp/templates/
COPY app.py /home/osboxes/ipa2025-msapp

EXPOSE 8080

CMD python /home/osboxes/ipa2025-msapp/app.py