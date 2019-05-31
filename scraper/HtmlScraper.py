import common.utils as utils
from common.KafkaProducerWrapper import KafkaProducerWrapper
import common.configurations as configurations


class HtmlScraper:

    def __init__(self, host):
        self.producer = KafkaProducerWrapper(host)

    def process_link(self, video_url):
        try:
            html = utils.fetch_html(video_url)

            self.producer.publish_message(configurations.YOUTUBE_PAGES_TOPIC, video_url, html)

        except Exception as ex:
            print('Exception in process_link')
            print(str(ex))


