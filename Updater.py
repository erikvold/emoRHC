#! /bin/python

import urllib
from bs4 import BeautifulSoup

location, message = urllib.urlretrieve('http://peter.sh/experiments/chromium-command-line-switches/')
with open (location, 'r') as f:
    soup = BeautifulSoup(f)

argumentsDescriptions = []
for table in soup.find_all('table', { 'class' : 'overview-table' }):
    for row in table.find_all('tr'):
        i = 0
        for cell in row.find_all('td'):
            if i == 0: i = cell.text
            else: argumentsDescriptions.append([i[:-2], cell.text[:-2]])

with open('chrome', 'w') as f:
    f.write('''#!/bin/sh

exec /usr/bin/google-chrome \\\n''')
    for argumentDescription in argumentsDescriptions:
        argument = argumentDescription[0]
        description = argumentDescription[1]
        f.write('# ' + description + '\n' + '#' + argument + ' \\\n')
    f.write('$@')