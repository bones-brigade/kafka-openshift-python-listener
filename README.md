# kafka-openshift-python-listener

A simple Python application that will listen to an Apache Kafka topic and print
messages that arrive on a specified topic.

it is designed for use with the [OpenShift](https://openshift.org)
[Python source-to-image](https://docs.openshift.org/latest/using_images/s2i_images/python.html)
workflow.

## Launching on OpenShift

```
oc new-app centos/python-36-centos7~https://github.com/bones-brigade/kafka-openshift-python-listener.git \
  -e SERVERS={broker} \
  -e TOPIC={topic} \
  --name=listener
```

Where `{broker}` is the uri for the Kafka broker (eg `my-broker:9092`), and
`{topic}` is the Kafka topic you would like to monitor.

After launching the application, you will most likely want to follow its log
output to see the messages it has heard.

```
oc logs -f dc/listener
```
