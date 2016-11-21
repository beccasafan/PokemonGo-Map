import config
from logger import log
import web_server
from models import Migration
from threading import Thread
import sys


# Patch to make exceptions in threads cause an exception.
def install_thread_excepthook():
    """
    Workaround for sys.excepthook thread bug
    (https://sourceforge.net/tracker/?func=detail&atid=105470&aid=1230540&group_id=5470).
    Call once from __main__ before creating any threads.
    If using psyco, call psycho.cannotcompile(threading.Thread.run)
    since this replaces a new-style class method.
    """
    import sys
    run_old = Thread.run

    def run(*args, **kwargs):
        try:
            run_old(*args, **kwargs)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            sys.excepthook(*sys.exc_info())
    Thread.run = run


# Exception handler will log unhandled exceptions
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    log.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def init():
    log.info('Starting')

    # Path threading to make exceptions catchable
    install_thread_excepthook()

    # Make sure exceptions get logged 
    sys.excepthook = handle_exception

    Migration.verify_schema()

    # keep alive for --web-is-server handled in the module, so just start
    web_server.start()

if __name__ == '__main__':
    init()
