import datetime
import logging
import sys
import re
from config import *
logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

requests_log = logging.getLogger("logparser")
requests_log.setLevel(logging.INFO)

def str_to_date(str):
    try:
        return datetime.datetime.strptime(str, '%d/%b/%Y:%H:%M:%S').date().isoformat()
    except ValueError:
        logger.warn(sys.exc_info()[1])
        return '1970-01-01'

def parse_nginx_log(line):
    regex = re.compile(nginx_log_pattern)
    try:
        column_names = [
            'ip_address',
            'date',
            'http_request_body',
            'status_code',
            'bytes',
            'referrer',
            'user_agent',
            'http_method'
        ]
        parsed_line = list(regex.findall(line)[0])
        # print parsed_line
        parsed_line[1] = str_to_date(parsed_line[1])
        parsed_line.append(parsed_line[2].split()[0])
    except:
        logger.error('Error while processing line:' + str(sys.exc_info()[1]))
        print line
    return dict(zip(column_names,parsed_line))