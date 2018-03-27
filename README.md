# kafka-openshift-python-listener

A simple Python application that will listen to an Apache Kafka topic and print
messages that arrive on a specified topic.

it is designed for use with the [OpenShift](https://openshift.org)
[Python source-to-image](https://docs.openshift.org/latest/using_images/s2i_images/python.html)
workflow.

## Launching on OpenShift

```
oc new-app centos/python-36-centos7~https://github.com/bones-brigade/kafka-openshift-python-listener.git \
  -e KAFKA_BROKERS=kafka:9092 \
  -e KAFKA_TOPIC=bones-brigade \
  --name=listener
```

You will need to adjust the `KAFKA_BROKERS` and `KAFKA_TOPICS` variables to
match your configured Kafka deployment and desired topic.

After launching the application, you will most likely want to follow its log
output to see the messages it has heard.

```
oc logs -f dc/listener
```
