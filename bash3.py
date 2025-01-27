from PIL import Image, ImageFilter

# Открываем изображение
image = Image.open('input_image.jpg')

# Пример 1: Изменение размера изображения
new_size = (800, 600)  # Новый размер (ширина, высота)
resized_image = image.resize(new_size)

# Пример 2: Применение эффекта размытия
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))

# Пример 3: Преобразование изображения в черно-белое
grayscale_image = image.convert('L')

# Сохранение обработанных изображений
resized_image.save('resized_image.jpg')
blurred_image.save('blurred_image.jpg')
grayscale_image.save('grayscale_image.jpg')

# Показ изображений (опционально)
resized_image.show(title="Измененный размер")
blurred_image.show(title="Размытое изображение")
grayscale_image.show(title="Черно-белое изображение")