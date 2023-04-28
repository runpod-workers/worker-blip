<div align="center">

<h1>BLIP | Worker</h1>

</div>

# Bliper-Serverless

This API provides an image captioning service that takes an image or a zip file containing multiple images and generates a caption for each image. The captions are saved into text files named after the input images and packed into a zip file for download.

## API Parameters

The API accepts the following parameters:

- `data_url` (required, string): The URL of the image or zip file containing multiple images to be captioned. The supported image formats are JPEG and PNG.

- `max_length` (optional, integer, default: 75): The maximum length of the generated captions. It should be a positive integer.

- `min_length` (optional, integer, default: 5): The minimum length of the generated captions. It should be a positive integer.

## API Output

The API returns a JSON object containing the following fields:

- `captions_zip_url`: The URL of the zip file containing the generated captions. Each caption is saved in a text file named after the input image (e.g., `input_image.jpg` will have a corresponding caption file named `input_image.txt`).
