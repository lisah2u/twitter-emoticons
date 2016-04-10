#!/usr/bin/env python

import sys
import json
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)


def convert_emoji():

    """
Converts escaped unicode in a dumped twitter JSON file to display in utf-8

    """


    # process a JSON file that contains a list of statuses
    #t = sys.stdin.read()
    #json_string = json.loads(t) # Takes a list of statuses
    #text = json.dumps(json_string, ensure_ascii=False)\
    #    .encode('utf16', "surrogatepass").decode("utf16")

    # process a file of JSON where each line is a status

    t = sys.stdin.readline()
    json_string = json.loads(t)
    text = json.dumps(json_string, ensure_ascii=False).encode('utf16', "surrogatepass").decode("utf16")

    sys.stdout.write(text)

if __name__ == "__main__":
    convert_emoji()
