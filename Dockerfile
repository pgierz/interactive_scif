FROM quay.io/scif/scif:latest

# Install questionary
RUN pip install questionary

COPY questionary_demo.scif /tmp/questionary_demo.scif

RUN scif install /tmp/questionary_demo.scif

COPY questionary_demo.py /scif/apps/questionary_demo/bin
RUN chmod +x /scif/apps/questionary_demo/bin/questionary_demo.py

# ENTRYPOINT ["scif"]
ENTRYPOINT ["python", "/scif/apps/questionary_demo/bin/questionary_demo.py"]


