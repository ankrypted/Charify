charsToUse = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def map_pixels(image, range_width=25):
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [charsToUse[pixel_value/range_width] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)
