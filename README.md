# Steganography CLI

CLI tool for encoding and decoding messages in images using Least Significant Bit (LSB) steganography, with support for encryption and various image formats.

## Features

- **LSB Steganography**: Encode and decode messages in images using the least significant bit technique.
- **Multiple Image Formats**: Support for encoding and decoding in various image formats (PNG, JPEG, etc.).

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
steganography encode <image_path> <message> <output_path>
```

Example:
```bash
steganography encode input.png "This is a hidden message" output.png
```

### Decoding a Message

To decode a message from an image:
```bash
steganography decode <image_path>
```

Example:
```bash
steganography decode output.png
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
