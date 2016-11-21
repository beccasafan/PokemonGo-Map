import logging
import config


logging.basicConfig(format='%(asctime)s [%(threadName)16s][%(module)14s][%(levelname)8s] %(message)s')
log = logging.getLogger()

# TODO: add file logging

verbose = config.get_arg('verbose')
very_verbose = config.get_arg('very_verbose')

log.setLevel(logging.DEBUG if verbose or very_verbose else logging.INFO)

logging.getLogger('pgoapi').setLevel(logging.DEBUG if verbose or very_verbose else logging.WARNING)
logging.getLogger('peewee').setLevel(logging.DEBUG if very_verbose else logging.INFO)
logging.getLogger('requests').setLevel(logging.DEBUG if very_verbose else logging.INFO)
logging.getLogger('pgoapi.pgoapi').setLevel(logging.DEBUG if very_verbose else logging.WARNING)
logging.getLogger('pgoapi.rpc_api').setLevel(logging.DEBUG if very_verbose else logging.INFO)
logging.getLogger('rpc_api').setLevel(logging.DEBUG if very_verbose else logging.WARNING)
logging.getLogger('werkzeug').setLevel(logging.DEBUG if very_verbose else logging.ERROR)
