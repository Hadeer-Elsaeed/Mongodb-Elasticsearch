FROM docker.elastic.co/logstash/logstash:7.15.1  

RUN rm -f /usr/share/logstash/pipeline/logstash.conf

# Install MongoDB input plugin  
RUN logstash-plugin install logstash-input-mongodb   

# Install Elasticsearch output plugin  
RUN logstash-plugin install logstash-output-elasticsearch  

# Copy the Logstash configuration file  
COPY logstash/pipeline/logstash.conf /usr/share/logstash/pipeline/logstash.conf  

# Run Logstash  
CMD ["logstash", "-f", "/usr/share/logstash/pipeline/logstash.conf"]
