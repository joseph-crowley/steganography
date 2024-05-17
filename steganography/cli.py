import click
from steganography.steganography import encode_message, decode_message

@click.group()
def cli() -> None:
    """A command-line interface for steganography."""
    pass

@cli.command()
@click.argument('image_path')
@click.argument('message')
@click.argument('output_path')
def encode(image_path: str, message: str, output_path: str) -> None:
    """Encode a MESSAGE into an IMAGE and save as OUTPUT_PATH."""
    try:
        encode_message(image_path, message, output_path)
    except ValueError as e:
        print(f"Error: {e}")

@cli.command()
@click.argument('image_path')
def decode(image_path: str) -> None:
    """Decode a message from an IMAGE."""
    try:
        decode_message(image_path)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    cli()
