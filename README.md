# qr-code-generator

A quick Python script to generate a high-resolution QR code for printing.

I originally wrote this to make a photo drop bucket for my wedding because:

- I didn’t want to pay a photographer, and
- I refused to pay for a QR code that wasn’t blurry at 8×10.

## Features

- CLI tool
- Outputs a **3000x3000 PNG** at **300 DPI** — perfect for printing
- Input your data (URL or text), get a QR image

## Usage

python3 main.py --data "https://example.com" --output "qr.png"
