import scaleImage as si
import mapPixels as mp
import conversionToGray as cg

def convert_image(image, modifiedWidth = 100):
	image = si.scale_image(image)
	image = cg.conversion_to_gray(image)
	pixel_to_chars = mp.map_pixels(image)
	len_pixel_to_chars = len(pixel_to_chars)
	print(len_pixel_to_chars)

	image_encode = [pixel_to_chars[index: index + modifiedWidth] for index in xrange(0, len_pixel_to_chars, modifiedWidth)]

	return "\n".join(image_encode)
