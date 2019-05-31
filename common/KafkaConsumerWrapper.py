from kafka import KafkaConsumer
import atexit

class KafkaConsumerWrapper:

    def __init__(self, host, topic_name):
        self.consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest',
                                                  bootstrap_servers=[f'{host}:9092'],
                                                  enable_auto_commit=True,
                                                  consumer_timeout_ms=1000)
        atexit.register(self.__close_connection)

    def start_consuming(self):


    def __close_connection(self):
        self.consumer.close()


