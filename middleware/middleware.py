import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class CountRequestsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.count_requests = 0
        self.count_exceptions = 0

    def __call__(self, request, *args, **kwargs):
        self.count_requests += 1
        logger.info(f"Handled {self.count_requests} requests so far")
        return self.get_response(request)

    def process_exception(self, request, exception):
        self.count_exceptions += 1
        logger.error(f"Encountered {self.count_exceptions} exceptions so far")
