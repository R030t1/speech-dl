#!/usr/bin/env python3
import os, sys, requests
from html.parser import HTMLParser

class HTMLContentParser(HTMLParser):
    def __init__(self):
        self.output_file   = None
        self.outro_nesting = 0
        super(HTMLContentParser, self).__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            if len(attrs) < 1:
                return

            # The inaugural address page is formatted differently, but contains
            # this div class.
            if 'field-type-text-long' in attrs[0][1]:
                self.outro_nesting = 2

    def handle_endtag(self, tag):
        if tag == 'div':
            self.outro_nesting -= 1

    def handle_data(self, data):
        if self.outro_nesting > 0:

            # There is lots of space in the output - leave it?
            print(data, file=self.output_file)

def main():
    base_dir = sys.argv[1]
    out_dir  = sys.argv[2]
    parser   = HTMLContentParser()

    for speech in os.listdir(base_dir):
        stripped = open(out_dir.rstrip('/') + '/' + speech, 'w')
        speech   = open(base_dir.rstrip('/') + '/' + speech)

        parser.output_file = stripped
        parser.feed(speech.read())
        
        parser.output_file.close()
        parser.reset()

if __name__ == '__main__':
    main()
