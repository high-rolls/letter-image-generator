# Letter Image Generator

This Flask application generates an image featuring the first letter of a given name. The letter is centered within a square image, and the font is customizable. You can specify the name via a URL parameter, and the app will respond with an image that contains the first letter of the name.

## Features

- Generates an image with the first letter of a given name.
- Customizable font (default font is used if a custom font is not available).
- Returns the image in PNG format.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abdelhakim-sahifa/letter-image-generator.git
   cd letter-image-generator
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Ensure you have the necessary font file (`Kagitingan-Bold.otf`) in the `fonts` directory or adjust the path in the code.

## Usage

Run the Flask application:

```bash
python app.py
```

The app will run locally, and you can access the endpoint:

```
http://127.0.0.1:5000//generate_image?name=John
```

Replace `John` with any name, and the app will return an image with the first letter of that name.

## Example

- Request:
  ```
  http://127.0.0.1:5000//generate_image?name=John
  ```
- Response: An image with the letter 'J' centered on a white background.

## Contributing

Feel free to open issues or pull requests for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
