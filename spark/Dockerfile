ARG SPARK_TAG
FROM apache/spark:${SPARK_TAG:-latest}

# Coordinates to install the necessary extensions.
ARG NESSIE_COORD
ARG ICEBERG_COORD
ARG AWSSDK_COORD
ARG AWS_URL_CONN_COORD

USER root

COPY --chmod=755 ./install-jar.py /bin/install-jar

RUN install-jar ${NESSIE_COORD} /opt/spark/jars
RUN install-jar ${ICEBERG_COORD} /opt/spark/jars
RUN install-jar ${AWSSDK_COORD} /opt/spark/jars
RUN install-jar ${AWS_URL_CONN_COORD} /opt/spark/jars
