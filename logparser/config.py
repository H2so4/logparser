nginx_log_pattern = '(?P<ipaddress>\d+\.\d+\.\d+\.\d+) [\w\W]+ [\w\W]+ \[(?P<timestamp>\d{2}\/[A-Za-z]+\/\d{4}:\d{2}:\d{2}:\d{2}) [-+]\d{4}\] "(?P<http_request_body>.*)" (?P<status_code>\d+) (?P<bytes>\d+) "(?P<referrer>.*)" "(?P<user_agent>.+)"'

parsers = {'nginx_log':nginx_log_pattern}