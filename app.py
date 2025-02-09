from flask import Flask, send_file, request
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/generate_image', methods=['GET'])
def generate_image():
    name = request.args.get('name', default='A', type=str)
    
    # Get the first letter of the name
    first_letter = name[0].upper()

    # Create an image with a white background
    img = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(img)

    # Load a font
    try:
        font = ImageFont.truetype("fonts\Kagitingan-Bold.otf",200)
    except IOError:
        font = ImageFont.load_default()

    # Get the bounding box of the text
    bbox = draw.textbbox((0, 0), first_letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate the position to center the text
    position = ((200 - text_width) / 2, (200 - text_height) / 2)

    # Draw the text on the image
    draw.text(position, first_letter, fill="black", font=font)

    # Save the image to a bytes buffer
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    # Return the image as a response
    return send_file(img_byte_array, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
