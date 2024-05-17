import click
import logging
from steganography.steganography import encode_message, decode_message

@click.group()
def cli() -> None:
    """A command-line interface for steganography."""
    pass

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.argument('message')
@click.argument('output_path', type=click.Path())
def encode(image_path: str, message: str, output_path: str) -> None:
    """Encode a MESSAGE into an IMAGE and save as OUTPUT_PATH."""
    try:
        encode_message(image_path, message, output_path)
    except ValueError as e:
        logging.error(f"Error: {e}")

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
def decode(image_path: str) -> None:
    """Decode a message from an IMAGE."""
    try:
        message = decode_message(image_path)
        if message:
            print(f"Decoded message: {message}")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    cli()

