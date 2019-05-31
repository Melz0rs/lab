from common.KafkaConsumerWrapper import KafkaConsumerWrapper
from scraper.HtmlScraper import HtmlScraper
import common.configurations as configurations


def scrape_first_video():
    video_url = 'https://www.youtube.com/watch?v=9sTQ0QdkN3Q'

    scraper.process_link(video_url)


def consume_youtube_link(link):
    scraper.process_link(link)


if __name__ == '__main__':
    scraper = HtmlScraper(configurations.ZOOKEEPER_HOST)
    consumer = KafkaConsumerWrapper(configurations.ZOOKEEPER_HOST, configurations.YOUTUBE_PAGES_TOPIC)

    scrape_first_video()
    consumer.start_consuming()

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36
    #     (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    #     'Pragma': 'no-cache'
    # }

    # if len(all_recipes) > 0:
    #     kafka_producer = connect_kafka_producer()
    #     for recipe in all_recipes:
    #         publish_message(kafka_producer, 'raw_recipes', 'raw', recipe.strip())
    #     if kafka_producer is not None:
    #         kafka_producer.close()
