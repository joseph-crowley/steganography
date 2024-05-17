from PIL import Image

DELIMITER = "~END~"

def encode_message(image_path: str, message: str, output_path: str) -> None:
    """Encode a message into an image and save it."""
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    encoded_image = encode_image(image, message + DELIMITER)
    encoded_image.save(output_path, format='PNG')
    print(f"Encoded image saved to {output_path}")

def decode_message(image_path: str) -> None:
    """Decode a message from an image."""
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    message = decode_image(image)
    if DELIMITER in message:
        message = message.split(DELIMITER)[0]
    print(f"Decoded message: {message}")

def encode_image(image: Image.Image, message: str) -> Image.Image:
    """Encode a message into an image."""
    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGBA')
        
    pixels = image.load()
    binary_message = ''.join([format(ord(c), '08b') for c in message])
    message_len = len(binary_message)
    width, height = image.size

    if message_len > width * height * 3:
        raise ValueError("Message is too long to be encoded in the given image")

    binary_message += '0' * (width * height * 3 - message_len)
    idx = 0

    for y in range(height):
        for x in range(width):
            r, g, b, *a = pixels[x, y]
            if idx < message_len:
                r = (r & ~1) | int(binary_message[idx])
                idx += 1
            if idx < message_len:
                g = (g & ~1) | int(binary_message[idx])
                idx += 1
            if idx < message_len:
                b = (b & ~1) | int(binary_message[idx])
                idx += 1
            if a:
                pixels[x, y] = (r, g, b, a[0])
            else:
                pixels[x, y] = (r, g, b)

    return image

def decode_image(image: Image.Image) -> str:
    """Decode a message from an image."""
    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGBA')

    pixels = image.load()
    width, height = image.size
    binary_message = ""

    for y in range(height):
        for x in range(width):
            r, g, b, *a = pixels[x, y]
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        message += char
        if DELIMITER in message:
            message = message.split(DELIMITER)[0]
            break

    return message
