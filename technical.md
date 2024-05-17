# Technical Documentation

## Steganography Method

This tool uses Least Significant Bit (LSB) steganography to encode and decode messages in images. LSB steganography works by manipulating the least significant bits of the pixel values in an image to embed the message.

### Encoding Process

1. Convert the message to a binary string.
2. Open the image and access its pixel data.
3. Replace the least significant bit of each pixel's RGB values or the alpha channel values with the message bits, depending on the specified mode.
4. Save the modified image.

### Decoding Process

1. Open the image and access its pixel data.
2. Extract the least significant bit of each pixel's RGB values or the alpha channel values, depending on the specified mode.
3. Combine these bits to reconstruct the binary representation of the message.
4. Convert the binary string back to text.

## Code Structure

### `steganography/steganography.py`

Contains the core functions for encoding and decoding messages:
- `encode_message(image_path: str, message: str, output_path: str, mode: str = 'rgb') -> None`
  - Encodes a message into an image file and saves it. Supports encoding in RGB channels or alpha channel based on the `mode` parameter.
  
- `decode_message(image_path: str, mode: str = 'rgb', use_delimiter: bool = False, delimiter: Optional[str] = None) -> Optional[str]`
  - Decodes a message from an image file. Supports decoding from RGB channels or alpha channel based on the `mode` parameter. Can use a delimiter to identify the end of the message.

- `encode_image(image: Image.Image, message: str, mode: str = 'rgb') -> Image.Image`
  - Encodes a message into a `PIL.Image` object. Supports encoding in RGB channels or alpha channel.

- `decode_image(image: Image.Image, mode: str = 'rgb', use_delimiter: bool = False, delimiter: Optional[str] = None) -> str`
  - Decodes a message from a `PIL.Image` object. Supports decoding from RGB channels or alpha channel. Can use a delimiter to identify the end of the message.

### `steganography/cli.py`

Defines the command-line interface using the `click` library:
- `encode(image_path, message, output_path, mode)`
  - Encodes a message into an image and saves it to the specified output path. Includes an option to specify the encoding mode (`rgb` or `alpha`).

- `decode(image_path, mode, use_delimiter, delimiter)`
  - Decodes a message from an image. Includes options to specify the decoding mode (`rgb` or `alpha`), whether to use a delimiter, and the delimiter to use.

## Additional Details

### Delimiters

The tool supports the use of delimiters to mark the end of encoded messages. This allows for more flexible message lengths and ensures that the entire message can be accurately decoded even if it doesn't perfectly fit the image size.

### Image Modes

- **RGB Mode**: Encodes the message in the least significant bits of the RGB channels of each pixel.
- **Alpha Mode**: Encodes the message in the least significant bits of the alpha channel of each pixel (for images with an alpha channel).

### Error Handling

- **Message Length**: The tool checks if the message is too long to be encoded in the given image dimensions and raises a `ValueError` if the message is too long.
- **Image Format**: The tool supports various image formats (e.g., PNG, JPEG) and handles format conversion as needed.
- **Delimiter Usage**: If a delimiter is used, the tool ensures that the message is correctly terminated at the delimiter during decoding.

By following these methods and structures, the Steganography CLI provides a robust and flexible tool for encoding and decoding hidden messages in images using LSB steganography.
