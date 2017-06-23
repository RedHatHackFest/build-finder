oc new-app --template=oshinko-pyspark-build-dc \
           -p APPLICATION_NAME=build-finder \
           -p GIT_URI=https://github.com/redhathackfest/build-finder \
           -p APP_ARGS='--bootstrap-servers=kafka:9092 --in=eventrouter --out=builds'  \
           -p SPARK_OPTIONS='--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.0'