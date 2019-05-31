from kafka import KafkaProducer
import atexit


class KafkaProducerWrapper:

    def __init__(self, zookeeper_host):
        self.producer = KafkaProducer(bootstrap_servers=[f'{zookeeper_host}:9092'])
        atexit.register(self.__close_connection)

    def publish_message(self, topic_name, key, value):
        try:
            key_bytes = bytes(key, encoding='utf-8')
            value_bytes = bytes(value, encoding='utf-8')
            self.producer.send(topic_name, key=key_bytes, value=value_bytes)
            self.producer.flush()
            print('Message published successfully.')

        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))

    def __close_connection(self):
        self.producer.close()
