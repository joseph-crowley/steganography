import unittest
from PIL import Image
from steganography.steganography import encode_image, decode_image, DELIMITER
import logging

# Configure logging to display debug messages during tests
logging.basicConfig(level=logging.DEBUG)

class TestSteganography(unittest.TestCase):
    """Test cases for the steganography module."""

    def setUp(self) -> None:
        """Set up the test fixtures."""
        self.message = "Hello"
        self.long_message = "This message is definitely too long for the image size"
        self.delimiter_message = self.message + DELIMITER

    def create_image(self, mode: str, size: tuple, color: str) -> Image.Image:
        """Helper method to create an image."""
        return Image.new(mode, size, color)

    def test_encode_decode_rgb(self) -> None:
        """Test encoding and decoding a message in an RGB image."""
        img = self.create_image('RGB', (50, 50), 'white')
        encoded_img = encode_image(img, self.delimiter_message)
        decoded_message = decode_image(encoded_img)
        self.assertEqual(decoded_message, self.message, "Decoded message does not match the original")

    def test_message_too_long(self) -> None:
        """Test encoding a message that is too long for the image."""
        img = self.create_image('RGB', (5, 5), 'white')
        with self.assertRaises(ValueError, msg="ValueError not raised for long message"):
            encode_image(img, self.long_message + DELIMITER)

    def test_non_rgb_image(self) -> None:
        """Test encoding and decoding a message in a non-RGB image."""
        img = self.create_image('L', (50, 50), 'white')  # Grayscale image
        encoded_img = encode_image(img, self.delimiter_message)
        decoded_message = decode_image(encoded_img)
        self.assertEqual(decoded_message, self.message, "Decoded message does not match the original")

    def test_encode_decode_rgba(self) -> None:
        """Test encoding and decoding a message in an RGBA image."""
        img = self.create_image('RGBA', (50, 50), 'white')
        encoded_img = encode_image(img, self.delimiter_message)
        decoded_message = decode_image(encoded_img)
        self.assertEqual(decoded_message, self.message, "Decoded message does not match the original")

    def test_multiple_messages(self) -> None:
        """Test encoding and decoding multiple messages in different images."""
        img1 = self.create_image('RGB', (50, 50), 'white')
        img2 = self.create_image('RGB', (50, 50), 'black')
        
        encoded_img1 = encode_image(img1, "Message1" + DELIMITER)
        encoded_img2 = encode_image(img2, "Message2" + DELIMITER)

        decoded_message1 = decode_image(encoded_img1)
        decoded_message2 = decode_image(encoded_img2)

        self.assertEqual(decoded_message1, "Message1", "Decoded message1 does not match the original")
        self.assertEqual(decoded_message2, "Message2", "Decoded message2 does not match the original")

    def tearDown(self) -> None:
        """Clean up after each test."""
        logging.debug("Test completed.")

if __name__ == '__main__':
    unittest.main()
