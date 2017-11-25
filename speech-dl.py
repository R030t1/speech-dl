#!/usr/bin/env python3
import sys, time, requests

base_dir = 'speeches-html'
base_url = 'https://whitehouse.gov'

def main():
    count = 0

    for url in open(sys.argv[1]):
        print(count, url.strip(), file=sys.stderr)

        save = open(base_dir + '/' + url.strip().rsplit('/', 1)[-1], 'w')
        page = requests.get(base_url + url.strip())
       
        save.write(page.text)
        save.close()

        count += 1
        time.sleep(5)

if __name__ == '__main__':
    main()
