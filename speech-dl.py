#!/usr/bin/env python3
import os, sys, time, requests

base_dir = 'speeches-html-2'
base_url = 'https://whitehouse.gov'

def main():
    count, name = 0, ''

    try:
        for url in sys.stdin:
            name = base_dir + '/' + str(count) + '_' + url.strip().rsplit('/', 2)[-2]
            if os.path.exists(name):
                count += 1
                continue

            print(count, url.strip(), file=sys.stderr)

            try:
                page = requests.get(base_url)
                save = open(name, 'w')

                save.write(page.text)
                save.close()
            except KeyboardInterrupt as kbi:
                os.remove(name)
                break
            except:
                pass
            finally:
                # On request timeout go to next page, intending
                # the program be re-run later.
                count += 1
                time.sleep(1)
    except:
        # Prevents Ctrl+C from leaving a file.
        # Sometimes we hit this from a weird place and get an exception.
        # Two KeyboardInterrupts while page is loading?
        os.remove(name)
        

if __name__ == '__main__':
    main()
