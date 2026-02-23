# PDF Filler Demo

A small Python CLI tool that fills PDF form fields using customer data from a JSON file.

## Overview
- Reads a template PDF (selected via `--form`)
- Loads customer records from `customers.json`
- Builds a PDF field/value map and fills the PDF
- Handles checkbox-style `/Btn` fields
- Optional: flattens the final PDF using Ghostscript (`--flatten`)
- Writes an output PDF named `{FirstName}_{LastName}_filled.pdf` (or `_flattened.pdf` when flattening is enabled)

## Important Note
All names and data in `customers.json` are **fake and for demo purposes only**.

## Requirements
- Python 3.x
- `pypdf`
- Optional for `--flatten`: Ghostscript (`gs` must be available on your PATH)

## Install
```bash
pip install pypdf
```

Usage

Basic:

python main.py --account 000000001

Choose a form:

python main.py --form test_spi.pdf --account 000000001

SPI instructions:

python main.py --form test_spi.pdf --account 000000001 --instructions ibp
python main.py --form test_spi.pdf --account 000000001 --instructions 1Etf
python main.py --form test_spi.pdf --account 000000001 --instructions 3Etf

Periodic investment frequency + start date:

python main.py --form test_pip.pdf --account 000000001 --frequency monthly --start_date 02/23/2026
python main.py --form test_pip.pdf --account 000000001 --frequency yearly --start_date 02/23/2026

Flatten output:

python main.py --form test_spi.pdf --account 000000001 --flatten

Valid values

--instructions: ibp, 1Etf, 3Etf
--frequency: monthly, yearly
--start_date: mm/dd/yyyy (example: 02/23/2026)

Logging

Logs are written to:

the console
pdf_filler.log
Notes
For the full, up-to-date list of CLI options, see get_customer.py.
Template-specific suppression logic (clearing certain fields based on selected options) lives in main.py.