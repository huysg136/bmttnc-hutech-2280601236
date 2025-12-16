import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    
    binary_message = ""

    for row in range(height):
        for col in range(width):
            
            pixel = img.getpixel((col, row))
            
            for color_channel in range(3):
                
                channel_value = pixel[color_channel]
                
                binary_message += format(channel_value, '08b')[-1]

    message = ""
    stop_marker = '1111111111111110'
    
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        
        if i + 16 <= len(binary_message):
            marker_check = binary_message[i:i+16]
            
            if marker_check == stop_marker:
                break
        
        char = chr(int(byte, 2))
        
        message += char
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    
    decoded_message = decode_image(encoded_image_path)
    
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()