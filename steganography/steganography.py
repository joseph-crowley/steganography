from PIL import Image
import logging
from typing import Optional

# Constant delimiter to indicate the end of the message
DEFAULT_DELIMITER = "~END~"

# Supported formats
SUPPORTED_FORMATS = {
    'jpeg': 'JPEG',
    'jpg': 'JPEG',
    'png': 'PNG',
    'bmp': 'BMP',
    'gif': 'GIF',
    'tiff': 'TIFF'
}

def encode_message(image_path: str, message: str, output_path: str, mode: str = 'rgb', output_format: Optional[str] = None) -> None:
    """
    Encode a message into an image and save it.

    Args:
        image_path (str): Path to the input image file.
        message (str): The message to encode into the image.
        output_path (str): Path to save the output image file.
        mode (str): The channel to use for encoding ('rgb' or 'alpha').
        output_format (Optional[str]): The format to save the output image in. If None, deduces from the output_path.

    Raises:
        FileNotFoundError: If the input image file is not found.
        Exception: If there is an error opening or processing the image.
    """
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        logging.error(f"The file {image_path} was not found.")
        return
    except Exception as e:
        logging.error(f"Error opening image: {e}")
        return

    try:
        encoded_image = encode_image(image, message + DEFAULT_DELIMITER, mode)
        if output_format is None:
            output_format = output_path.split('.')[-1].lower()
        if output_format not in SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported format: {output_format}")
        encoded_image.save(output_path, format=SUPPORTED_FORMATS[output_format])
        logging.info(f"Encoded image saved to {output_path} in format {SUPPORTED_FORMATS[output_format]}")
    except Exception as e:
        logging.error(f"Error encoding message: {e}")

def decode_message(image_path: str, mode: str = 'rgb', use_delimiter: bool = False, delimiter: Optional[str] = None) -> Optional[str]:
    """
    Decode a message from an image.

    Args:
        image_path (str): Path to the input image file.
        mode (str): The channel to use for decoding ('rgb' or 'alpha').
        use_delimiter (bool): Whether to use a delimiter to determine the end of the message.
        delimiter (Optional[str]): The delimiter to use if use_delimiter is True.

    Returns:
        Optional[str]: The decoded message if found, otherwise None.

    Raises:
        FileNotFoundError: If the input image file is not found.
        Exception: If there is an error opening or processing the image.
    """
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        logging.error(f"The file {image_path} was not found.")
        return None
    except Exception as e:
        logging.error(f"Error opening image: {e}")
        return None

    try:
        message = decode_image(image, mode, use_delimiter, delimiter if delimiter else DEFAULT_DELIMITER)
        logging.info(f"Decoded message: {message}")
        return message
    except Exception as e:
        logging.error(f"Error decoding message: {e}")
        return None

def encode_image(image: Image.Image, message: str, mode: str = 'rgb') -> Image.Image:
    """
    Encode a message into an image.

    Args:
        image (Image.Image): The image to encode the message into.
        message (str): The message to encode.
        mode (str): The channel to use for encoding ('rgb' or 'alpha').

    Returns:
        Image.Image: The image with the encoded message.

    Raises:
        ValueError: If the message is too long to be encoded in the given image.
    """
    if mode not in ('rgb', 'alpha'):
        raise ValueError("Mode must be 'rgb' or 'alpha'")

    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGBA')

    pixels = image.load()
    binary_message = ''.join([format(ord(c), '08b') for c in message])
    message_len = len(binary_message)
    width, height = image.size

    if mode == 'rgb' and message_len > width * height * 3:
        raise ValueError("Message is too long to be encoded in the given image in RGB mode")
    if mode == 'alpha' and message_len > width * height:
        raise ValueError("Message is too long to be encoded in the given image in Alpha mode")

    binary_message += '0' * (width * height * (3 if mode == 'rgb' else 1) - message_len)
    idx = 0

    for y in range(height):
        for x in range(width):
            r, g, b, *a = pixels[x, y]
            if mode == 'rgb':
                if idx < message_len:
                    r = (r & ~1) | int(binary_message[idx])
                    idx += 1
                if idx < message_len:
                    g = (g & ~1) | int(binary_message[idx])
                    idx += 1
                if idx < message_len:
                    b = (b & ~1) | int(binary_message[idx])
                    idx += 1
            elif mode == 'alpha' and a:
                if idx < message_len:
                    a[0] = (a[0] & ~1) | int(binary_message[idx])
                    idx += 1

            if a:
                pixels[x, y] = (r, g, b, a[0])
            else:
                pixels[x, y] = (r, g, b)

    return image

def decode_image(image: Image.Image, mode: str = 'rgb', use_delimiter: bool = False, delimiter: Optional[str] = None) -> str:
    """
    Decode a message from an image using LSB steganography.

    Args:
        image (Image.Image): The image to decode the message from.
        mode (str): The channel to use for decoding ('rgb' or 'alpha').
        use_delimiter (bool): Whether to use a delimiter to determine the end of the message.
        delimiter (Optional[str]): The delimiter to use if use_delimiter is True.

    Returns:
        str: The decoded message.
    """
    if mode not in ('rgb', 'alpha'):
        raise ValueError("Mode must be 'rgb' or 'alpha'")

    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGBA')

    pixels = image.load()
    width, height = image.size
    binary_message = ""

    for y in range(height):
        for x in range(width):
            if mode == 'rgb':
                r, g, b, *a = pixels[x, y]
                binary_message += str(r & 1)
                binary_message += str(g & 1)
                binary_message += str(b & 1)
            elif mode == 'alpha' and image.mode == 'RGBA':
                *_, a = pixels[x, y]
                binary_message += str(a & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) < 8:
            continue
        char = chr(int(byte, 2))

        if use_delimiter and delimiter:
            message += char
            if delimiter in message:
                message = message.split(delimiter)[0]
                break
        else:
            if byte == '00000000':
                break
            message += char

    return message
