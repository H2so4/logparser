from __future__ import absolute_import

opts = """Log parser - A simple tool to aggregate log entries.

Usage:
  logparser.py parse_nginx <name>...
  logparser.py --version

Options:
  -h --help     Show this screen.
  --verbose  Verbosity level [default: False].
"""
from docopt import docopt

from contextlib import contextmanager
import sys, os
from utils import parse_nginx_log
from collections import defaultdict
from multiprocessing import Pool
import pandas as pd

from gevent import pool as gpool
class workerPool:
    def __init__(self, processes):
        self.pool = Pool(processes)

    def __enter__(self):
        return self.pool

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pool.close()

log_file = '/Users/okezie/Documents/projects/python/logparser/accesslog_aggregate.log'
# log_file = '/Users/okezie/Documents/projects/python/logparser/tests/files/sample_log_file.log'
# for line in log_file:
#     parse(line)

chunk_size = 200000
process_count = 200

def stream_file(file_path):
    for line in open(file_path):
        yield line

def update_counters(entries):
    df = pd.DataFrame(entries)
    del entries
    return df

def print_stats(aggregator):
    by_date = aggregator.groupby('date')
    by_date_useragent = aggregator.groupby(['user_agent','date'])
    by_httpmethod_by_OS_by_day = aggregator.groupby(['user_agent','os','date'])
    total_requests_by_date = by_date['http_method'].count()
    frequent_useragents_by_date = by_date_useragent['user_agent'].count().to_dict().items()
    # x = by_httpmethod_by_OS_by_day.count()
    # print x.add_suffix('_Count').reset_index()
    print "=========== Total Requests by date ============="
    print total_requests_by_date.to_string()

    print "=========== Top 3 Requests by User agent by Date ============="
    top_3 =  sorted(frequent_useragents_by_date, key=lambda tup: tup[1], reverse=True)[:3]
    print 'Frequency\t\tDate\t\tUseragent'
    for user_agent_date,frequency in top_3:
        user_agent, date = user_agent_date
        print '{}\t\t\t{}\t\t\t{}'.format(frequency,date, user_agent)
    print '=' * 40




def main():
    with open(log_file) as fd:
        with workerPool(process_count) as pool:
            lines_to_process = []
            entries = []
            aggregator = None
            for i,line in enumerate(fd):
                lines_to_process.append(line)
                if len(lines_to_process) == chunk_size:
                    print "processing: " + i.__str__()
                    entries = pool.map(parse_nginx_log, lines_to_process)
                    # update_counters(entries, aggregator)
                    lines_to_process = []
            entries.extend(pool.map(parse_nginx_log, lines_to_process))
            # print entries
            aggregator = update_counters(entries)
            print print_stats(aggregator)
            del lines_to_process


if __name__ == '__main__':
    # arguments = docopt(opts, version='Naval Fate 2.0')
    # print(arguments)
    main()



