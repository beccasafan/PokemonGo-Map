from configargparse import ArgParser


parser = ArgParser(default_config_files=['config/config.ini'])

# Web Server
parser.add_argument('--web-host', type=str, action='store', default='127.0.0.1', help='Web server host ip')
parser.add_argument('--web-port', type=str, action='store', default=5000, help='Web server port')
parser.add_argument('--web-scanner', action='store_true', default=True, help='Run the scanner')
parser.add_argument('--web-server', action='store_true', default=True, help='Run the web server')

# Database
parser.add_argument('--db-type', type=str.lower, action='store', default='sqlite', help='Type of database (default: sqlite)')
parser.add_argument('--db-file-name', type=str, action='store', default='pogom.db', help='Name of the sqlite file')
parser.add_argument('--db-name', type=str, action='store', help='Name of the database')
parser.add_argument('--db-user', help='Username for the database')
parser.add_argument('--db-pass', help='Password for the database')
parser.add_argument('--db-host', help='IP or hostname for the database')
parser.add_argument('--db-port', help='Port for the database', type=int, default=3306)

# Instance
parser.add_argument('--verbose', action='store_true', default=False, help='Show debug messages from PomemonGo-Map and pgoapi.')  # TODO: optional file argument
parser.add_argument('--very-verbose', action='store_true', default=False, help='Like verbose, but show debug messages from all modules as well.')  # TODO: optional file argument
__args = parser.parse_args()

errors = []

if __args.db_type == 'mysql':
    if __args.db_name is None:
        errors.append('--db_name is required for mysql')
        # etc...

    # etc...

if (len(errors) > 0):
    for e in errors:
        print(e)
    exit()


def get_arg(arg):
    return getattr(__args, arg)
