import argparse
import qrcode
import qrcode.constants
from PIL import Image


DEFAULT_SIZE = 3000
DEFAULT_DPI = (300, 300)


def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((3000, 3000), resample=Image.LANCZOS)
    img.save(output_file, dpi=(300, 300))
    print(f"QR code saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Generate a high-resolution QR code image.")
    parser.add_argument("--data", required=True, help="The URL or text to encode in the QR code.")
    parser.add_argument("--output", default="qr_code.png", help="Filename to save the QR code image.")

    args = parser.parse_args()
    generate_qr_code(args.data, args.output)


if __name__ == "__main__":
    main()