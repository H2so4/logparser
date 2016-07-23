from __future__ import absolute_import
import sys,os,unittest
from mock import patch
import logging
import datetime
sys.path.append(os.path.dirname(__file__) + '/../logparser')

from utils import *

class TestLogparser(unittest.TestCase):
   def setUp(self):
       self.lines = open(os.path.dirname(__file__) + '/files/sample_log_file.log').readlines()


   def test_str_to_date(self):
       assert str_to_date('01/Foo/2011:06:31:44') == '1970-01-01'
       assert str_to_date('01/Dec/2011:06:31:44') == '2011-12-01'

   def test_parse_line(self):
        parsed_line = map(parse_nginx_log, self.lines)
        assert parsed_line == [
            {'referrer': 'http://aviflax.com/post/bukharian-jewish-cuisine-for-l/', 'bytes': '33473', 'ip_address': '127.0.0.1', 'http_method': 'GET', 'user_agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; YPC 3.0.2; .NET CLR 1.1.4322; yplus 4.4.02b)', 'status_code': '200', 'date': '2011-12-01', 'http_request_body': 'GET /post/bukharian-jewish-cuisine-for-l/ HTTP/1.0', 'os': 'windows'},
            {'referrer': '-', 'bytes': '227', 'http_method': 'POST', 'user_agent': 'WordPress/3.2.1; http://aviflax.com', 'status_code': '200', 'date': '2011-12-01', 'http_request_body': 'POST /wp-cron.php?doing_wp_cron HTTP/1.0', 'ip_address': '127.0.0.1'},
            {'referrer': 'http://aviflax.com/post/bukharian-jewish-cuisine-for-l/', 'bytes': '454', 'ip_address': '127.0.0.1', 'http_method': 'POST', 'user_agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; YPC 3.0.2; .NET CLR 1.1.4322; yplus 4.4.02b)', 'status_code': '302', 'date': '2011-12-01', 'http_request_body': 'POST /wp-comments-post.php HTTP/1.0', 'os': 'windows'},
            {'referrer': 'http://aviflax.com/post/bukharian-jewish-cuisine-for-l/', 'bytes': '33473', 'ip_address': '127.0.0.1', 'http_method': 'GET', 'user_agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; YPC 3.0.2; .NET CLR 1.1.4322; yplus 4.4.02b)', 'status_code': '200', 'date': '2011-12-01', 'http_request_body': 'GET /post/bukharian-jewish-cuisine-for-l/ HTTP/1.0', 'os': 'windows'},
            {'referrer': '-', 'bytes': '7990', 'http_method': 'GET', 'user_agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'status_code': '200', 'date': '2011-12-01', 'http_request_body': 'GET /post/strangeloop-ok-%E2%80%9Ccloud%E2%80%9D-h/ HTTP/1.0', 'ip_address': '127.0.0.1'},
            {'referrer': 'http://aviflax.com/post/twenty-five-songs/', 'bytes': '35426', 'ip_address': '127.0.0.1', 'http_method': 'GET', 'user_agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)', 'status_code': '200', 'date': '2011-12-01', 'http_request_body': 'GET /post/twenty-five-songs/ HTTP/1.0', 'os': 'windows'},
            {'referrer': 'http://aviflax.com/post/twenty-five-songs/', 'bytes': '441', 'ip_address': '127.0.0.1', 'http_method': 'POST', 'user_agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)', 'status_code': '302', 'date': '2011-12-01', 'http_request_body': 'POST /wp-comments-post.php HTTP/1.0', 'os': 'windows'},
            {'referrer': 'http://aviflax.com/post/twenty-five-songs/', 'bytes': '35426', 'ip_address': '127.0.0.1', 'http_method': 'GET', 'user_agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)', 'status_code': '200', 'date': '2011-12-01', 'http_request_body': 'GET /post/twenty-five-songs/ HTTP/1.0', 'os': 'windows'},
            {'referrer': '-', 'bytes': '9878', 'http_method': 'GET', 'user_agent': 'Sosospider+(+http://help.soso.com/webspider.htm)', 'status_code': '200', 'date': '1970-01-01', 'http_request_body': 'GET / HTTP/1.0', 'ip_address': '127.0.0.1'}
        ]
