import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image

def reduce_colors(image_path, num_colors):
    # Загрузка изображения и преобразование в массив пикселей
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = np.array(image).reshape(-1, 3)

    # Нормализация пикселей
    pixels = pixels.astype('float32') / 255.0

    # Применение кластеризации k-средних
    kmeans = KMeans(n_clusters=num_colors)
    labels = kmeans.fit_predict(pixels)

    # Создание палитры цветов
    palette = kmeans.cluster_centers_ * 255
    palette = palette.astype('uint8')

    # Замена пикселей на ближайший цвет из палитры
    new_pixels = palette[labels]

    # Преобразование массива пикселей обратно в изображение
    new_image = new_pixels.reshape(image.size[1], image.size[0], 3)  # Исправлено: изменен порядок пикселей
    new_image = new_image.astype('uint8')

    # Сохранение нового изображения
    new_image = Image.fromarray(new_image)
    new_image.save(f'output_{num_colors}_colors.png')

# Пример использования
image_path = 'fsd.png'
num_colors = 2
reduce_colors(image_path, num_colors)
