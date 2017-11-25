# speech-dl

Download the president's speeches from https://whitehouse.gov.

## Instructions

The downloaded HTML files are included in this repository. Assuming they are
not there or that there are new speeches, run:

* `./speech-enum > speech-links.txt`
* `./speech-dl speech-links.txt`

Then, run:

* `./speech-strip speeches-html speeches-text`

To remove the HTML tags from the speeches.

## TODO

* Do not redownload already present speeches.
