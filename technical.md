# Technical Documentation

## Steganography Method

This tool uses Least Significant Bit (LSB) steganography to encode and decode messages in images. LSB steganography works by manipulating the least significant bits of the pixel values in an image to embed the message.

### Encoding Process

1. Convert the message to a binary string.
2. Open the image and access its pixel data.
3. Replace the least significant bit of each pixel's RGB values with the message bits.
4. Save the modified image.

### Decoding Process

1. Open the image and access its pixel data.
2. Extract the least significant bit of each pixel's RGB values.
3. Combine these bits to reconstruct the binary representation of the message.
4. Convert the binary string back to text.

## Code Structure

### `steganography/steganography.py`

Contains the core functions for encoding and decoding messages:
- `encode_message(image_path: str, message: str, output_path: str)`
- `decode_message(image_path: str)`
- `encode_image(image, message)`
- `decode_image(image)`

### `steganography/cli.py`

Defines the command-line interface using the `click` library:
- `encode(image_path, message, output_path)`
- `decode(image_path)`
