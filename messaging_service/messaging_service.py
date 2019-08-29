import logging

from message_queue.message_queue_client import Receivers


class MessagingService(object):
    """
    Messaging Service class.
    """

    def __init__(self):
        self.rs = Receivers('messaging-service', [self.send_email])

    def start(self):
        logging.info('starting ...')
        self.rs.start()
        self.rs.wait()

    def stop(self):
        self.rs.stop()

    def send_email(self, _req):

        if not _req['to'] or not _req['msg']:
            return {
                "error": "missing mandatory parameter 'to' and/or 'msg'"
            }

        logging.info('sent email with message "{}" to "{}"'.format(_req['msg'], _req['to']))
        return {
            "result": True
        }


logging.basicConfig(level=logging.INFO)

m = MessagingService()
m.start()
