import click
import logging
from steganography.steganography import encode_message, decode_message
from typing import Optional

@click.group()
def cli() -> None:
    """A command-line interface for steganography."""
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.argument('message')
@click.argument('output_path', type=click.Path())
@click.option('--mode', type=click.Choice(['rgb', 'alpha']), default='rgb', help='The channel to use for encoding (default: rgb).')
def encode(image_path: str, message: str, output_path: str, mode: str) -> None:
    """Encode a MESSAGE into an IMAGE and save as OUTPUT_PATH."""
    try:
        encode_message(image_path, message, output_path, mode)
    except ValueError as e:
        logging.error(f"Error: {e}")

@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('--mode', type=click.Choice(['rgb', 'alpha']), default='rgb', help='The channel to use for decoding (default: rgb).')
@click.option('--use-delimiter', is_flag=True, default=False, help='Whether to use a delimiter to determine the end of the message.')
@click.option('--delimiter', type=str, default=None, help='The delimiter to use if use-delimiter is enabled (default: ~END~).')
def decode(image_path: str, mode: str, use_delimiter: bool, delimiter: Optional[str]) -> None:
    """Decode a message from an IMAGE."""
    try:
        message = decode_message(image_path, mode, use_delimiter, delimiter)
        if message:
            print(f"Decoded message: {message}")
        else:
            print("No message found or message is empty.")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    cli()
