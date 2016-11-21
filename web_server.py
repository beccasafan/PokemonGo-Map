
import config
from logger import log
import time

app = None

if config.get_arg('web_server'):
    from flask import Flask
    app = Flask(__name__)

    @app.route('/test')
    def test():
        return 'Testing...'


def start():
    """
    If instance is a web server, start Flask. Otherwise, create an endless while loop.
    """

    if config.get_arg('web_server'):
        log.info('Running flask')
        app.run(
            host=config.get_arg('web_host'),
            port=config.get_arg('web_port'),
            debug=False
        )
    else:
        log.info('Running keep-alive loop')
        while True:
            time.sleep(60)
