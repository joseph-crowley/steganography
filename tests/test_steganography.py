import unittest
from steganography.steganography import encode_image, decode_image, DELIMITER
from PIL import Image

class TestSteganography(unittest.TestCase):
    
    def test_encode_decode(self) -> None:
        # Create a simple test image (larger size)
        img = Image.new('RGB', (50, 50), color='white')
        
        # Encode a message
        message = "Hello"
        encoded_img = encode_image(img, message + DELIMITER)
        
        # Decode the message
        decoded_message = decode_image(encoded_img)
        
        # Assert the message is correctly decoded
        self.assertEqual(decoded_message, message)

    def test_message_too_long(self) -> None:
        img = Image.new('RGB', (5, 5), color='white')
        message = "This message is definitely too long for the image size"
        with self.assertRaises(ValueError):
            encode_image(img, message + DELIMITER)

    def test_non_rgb_image(self) -> None:
        img = Image.new('L', (50, 50), color='white')  # Grayscale image
        message = "Hello"
        encoded_img = encode_image(img, message + DELIMITER)
        decoded_message = decode_image(encoded_img)
        self.assertEqual(decoded_message, message)

if __name__ == '__main__':
    unittest.main()
