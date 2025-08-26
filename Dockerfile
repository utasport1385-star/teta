FROM earnfm/earnfm-client:latest
RUN apt-get update && apt-get install -y python3
COPY keepalive.py /keepalive.py
ENV EARNFM_TOKEN=adc9585e-dc61-44dd-8f39-3ee7bf03524b
EXPOSE 8080
CMD sh -c "earnfm-client & python3 /keepalive.py"
