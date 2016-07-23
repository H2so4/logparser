from __future__ import absolute_import

opts = """Log parser - A simple tool to aggregate log entries.

Usage:
  logparser nginx <file>
  logparser --version

Options:
  -h --help     Show this screen.
  --verbose  Verbosity level [default: False].
"""

from docopt import docopt
import sys, os
sys.path.append(os.path.dirname(__file__))
from utils import parse_nginx_log
from multiprocessing import Pool
import pandas as pd

class workerPool:
    def __init__(self, processes):
        self.pool = Pool(processes)

    def __enter__(self):
        return self.pool

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pool.close()

chunk_size = 200000
process_count = 200

def convert_to_dataframe(entries):
    df = pd.DataFrame(entries)
    del entries
    return df

def print_stats(log_df):
    '''
    Perform groupby operations on the pandas dataframe and print stats to stdout
    :param log_df:
    :return None:
    '''
    by_date = log_df.groupby('date')
    by_date_useragent = log_df.groupby(['user_agent','date'])
    by_httpmethod_by_OS_by_day = log_df.groupby(['user_agent','os','date'])
    total_requests_by_date = by_date['http_method'].count()
    frequent_useragents_by_date = by_date_useragent['user_agent'].count().to_dict().items()
    print "=========== Total Requests by date ============="
    print total_requests_by_date.to_string()

    print "=========== Top 3 Requests by User agent by Date ============="
    top_3 =  sorted(frequent_useragents_by_date, key=lambda tup: tup[1], reverse=True)[:3]
    print 'Frequency\t\tDate\t\tUseragent'
    for user_agent_date,frequency in top_3:
        user_agent, date = user_agent_date
        print '{}\t\t\t{}\t\t\t{}'.format(frequency,date, user_agent)
    print '=' * 40




def main(arguments):
    with open(arguments['<file>']) as fd:
        with workerPool(process_count) as pool:
            lines_to_process = []
            entries = []

            for i,line in enumerate(fd):
                lines_to_process.append(line)
                if len(lines_to_process) == chunk_size:
                    entries = pool.map(parse_nginx_log, lines_to_process)
                    lines_to_process = []

            entries.extend(pool.map(parse_nginx_log, lines_to_process))
            del lines_to_process
            log_df = convert_to_dataframe(entries)
            print_stats(log_df)

def get_opts():
    arguments = docopt(opts, version='Logparser 1.0')
    main(arguments)

if __name__ == '__main__':
    arguments = docopt(opts, version='Logparser 1.0')
    main(arguments)



