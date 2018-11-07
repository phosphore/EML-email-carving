# EML-email-carving
Extract "From", "To", "Cc", "Bcc" fields from .eml files (useful for email dumps/data carving/harvesting)

## Requirements
Requires Python 3 and [eml_parser](https://github.com/GOVCERT-LU/eml_parser) / eml_parser[file-magic].

## Note for OSX users
Make sure to install libmagic, else eml_parser will not work.

## Usage
Just put getEmails.py in the same/parent directory of the .eml files. At the end you'll have a mails.txt file containing every unique email address found in the metadata fields.

## CoC
Just use this tool for good and [do no harm](https://github.com/raisely/NoHarm).
