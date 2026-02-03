# PDF Filler Demo

This is a small Python script that programmatically fills a PDF form with customer data.
I used a demo "standing payment instructions" form as a test. 
I may include other **demo** forms in the future.
That was the purpose for including more data than was nessesary to fill in the spi form.

## Overview
- Reads a template PDF (`test_spi.pdf`) with form fields.
- Loads customer information from `customers.json`.
- Fills in the PDF fields and generates a new file (`filled_{first}_{last}_spi.pdf`).

## Purpose
This project is a **demo** to show Python scripting for backend/data automation tasks. It is **not production code**.

## Important Note
All names, account numbers, and other data in `customers.json` are **fake and for demonstration purposes only**.

## Usage
Run the script with an optional customer index:

```bash
python main.py --customer 0