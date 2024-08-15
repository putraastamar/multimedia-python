
from PIL import Image, ImageFilter

# Memuat gambar
image = Image.open('gambar.jpg')

# Menyimpan gambar
image.save('result.jpg')

# Cropping
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

# Resizing
resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')

# Filtering
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')
fg