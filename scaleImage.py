def scale_image(image, new_width=100):
	(original_width, original_height) = image.size
	print(original_height, original_height)
	aspect_ratio = original_height/float(original_width)
	new_height = int(aspect_ratio * new_width)
	new_image = image.resize((new_width, new_height))
	return new_image
