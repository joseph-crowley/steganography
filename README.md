# Steganography CLI

CLI tool for encoding and decoding messages in images using Least Significant Bit (LSB) steganography, with support for encryption and various image formats.

## Features

- **LSB Steganography**: Encode and decode messages in images using the least significant bit technique.
- **Multiple Image Formats**: Support for encoding and decoding in various image formats (PNG, JPEG, etc.).
- **Encoding Modes**: Support for encoding messages in RGB channels or the alpha channel of images.
- **Delimiters**: Use delimiters to mark the end of encoded messages.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/joseph-crowley/steganography.git
    ```

2. Navigate to the project directory:
    ```bash
    cd steganography
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Install the CLI tool:
    ```bash
    pip install .
    ```

## Usage

### Encoding a Message

To encode a message in an image:
```bash
steganography encode <image_path> <message> <output_path> [--mode <mode>]
```
- `<image_path>`: Path to the input image file.
- `<message>`: The message to encode into the image.
- `<output_path>`: Path to save the output image file.
- `--mode <mode>`: (Optional) The channel to use for encoding ('rgb' or 'alpha'). Default is 'rgb'.

Example:
```bash
steganography encode input.png "This is a hidden message" output.png --mode rgb
```

### Decoding a Message

To decode a message from an image:
```bash
steganography decode <image_path> [--mode <mode>] [--use-delimiter] [--delimiter <delimiter>]
```
- `<image_path>`: Path to the input image file.
- `--mode <mode>`: (Optional) The channel to use for decoding ('rgb' or 'alpha'). Default is 'rgb'.
- `--use-delimiter`: (Optional) Whether to use a delimiter to determine the end of the message.
- `--delimiter <delimiter>`: (Optional) The delimiter to use if `--use-delimiter` is enabled. Default is '~END~'.

Example:
```bash
steganography decode output.png --mode rgb --use-delimiter --delimiter "~END~"
```

## Testing

To run the tests:
```bash
python -m unittest discover tests
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.