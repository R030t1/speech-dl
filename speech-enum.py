#!/usr/bin/env python3
import sys, time, requests
from html.parser import HTMLParser

#base_url = 'https://www.whitehouse.gov/briefing-room/speeches-and-remarks?page='
#
#class HTMLAnchorParser(HTMLParser):
#    def __init__(self):
#        self.outro_nesting = 0
#        super(HTMLAnchorParser, self).__init__()
#
#    def handle_starttag(self, tag, attrs):
#        if tag == 'div':
#            if len(attrs) < 1:
#                return
#
#            if 'views-row' in attrs[0][1]:
#                self.outro_nesting = 2
#
#            if 'pane-press-office-listings-panel-pane-1' in attrs[0][1]:
#                self.in_brief = True
#        elif tag == 'a':
#            if self.outro_nesting > 0:
#                print(attrs[0][1])
#
#    def handle_endtag(self, tag):
#        if tag == 'div' and self.outro_nesting > 0:
#            self.outro_nesting -= 1
#
#    def handle_data(self, data):
#        pass

base_url = 'https://www.whitehouse.gov/briefings-statements/page/'

class HTMLAnchorParser(HTMLParser):
    def __init__(self):
        self.outro_nesting = 0
        super(HTMLAnchorParser, self).__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'h2' and attrs[0][1] == 'briefing-statement__title':
            self.outro_nesting = 1
        elif tag == 'a' and self.outro_nesting == 1:
            # Should be in endtag.
            self.outro_nesting -= 1
            print(attrs[0][1])

    def handle_endtag(self, tag):
        pass
        # The below doesn't work for some reason.
        #if tag == 'h2' and self.outro_nesting > 0:
        #    self.outro_nesting -= 1

    def handle_endtag(self, data):
        pass

def main():
    parser = HTMLAnchorParser()

    if len(sys.argv) > 2:
        start = int(sys.argv[2])
    else:
        start = 0

    for p in range(start, int(sys.argv[1])):
        print(p, file=sys.stderr)

        page = requests.get(base_url + str(p))
        parser.feed(page.text)
        parser.reset()

        sys.stdout.flush()
        time.sleep(5)

if __name__ == '__main__':
    main()
