#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('./domains.csv', 'r') as f:
    urls = {'\'' + url + '\'' for url in f.read().split('\n') if url}

with open('./domains.js', 'w') as f:
    f.write('blocklist.DOMAINS = [\n')
    f.write(',\n'.join(sorted(list(urls))))
    f.write('];\n')

# blocklist.DOMAINS = [];
