#!/usr/bin/env python
"""build-finder
This app will find OpenShift Builds in a stream of events on a kafka topic,
all found Builds will be send them to another topic.
"""

import time
import argparse
import json

import kafka
#import pyspark
#from pyspark import streaming
#from pyspark.streaming import kafka as kstreaming
from prometheus_client import start_http_server, Counter

build_counter = Counter('openshift_builds_total', 'Total number of OpenShift Builds found')

def main():
    """The main function
    This will process the command line arguments and launch the main
    Spark/Kafka app class.
    """
    parser = argparse.ArgumentParser(description='process data with Spark, using Kafka as the transport')
    parser.add_argument('--in', dest='input_topic', help='the kafka topic to read data from')
    parser.add_argument('--out', dest='output_topic', help='the kafka topic to publish data to')
    parser.add_argument('--bootstrap-servers', dest='servers', help='the kafka bootstrap servers')
    args = parser.parse_args()

    while True:
        time.sleep(1)

if __name__ == '__main__':
    start_http_server(8080)

    main()