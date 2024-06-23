from PIL import Image, ImageDraw

# Определение цветов для гласных, согласных и знаков препинания
vowel_colors = ['#FFFF00', '#FFA500', '#FF0000']  # Желтый, оранжевый, красный
consonant_colors = ['#008000', '#00FFFF', '#0000FF', '#800080']  # Зеленый, голубой, синий, фиолетовый
punctuation_colors = ['#808080']  # Серый


vowels = "аеёиоуыэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"
punctuations = ".,:;!?-—()«»\""


def create_color_dict(chars, colors):
    char_count = len(chars)
    color_dict = {}
    for i, char in enumerate(chars):
        color_dict[char] = colors[i * len(colors) // char_count]
    return color_dict


vowel_color_dict = create_color_dict(vowels, vowel_colors)
consonant_color_dict = create_color_dict(consonants, consonant_colors)
punctuation_color_dict = create_color_dict(punctuations, punctuation_colors)

def get_color(char):
    lower_char = char.lower()
    if lower_char in vowel_color_dict:
        return vowel_color_dict[lower_char]
    elif lower_char in consonant_color_dict:
        return consonant_color_dict[lower_char]
    elif lower_char in punctuation_color_dict:
        return punctuation_color_dict[lower_char]
    else:
        return '#FFFFFF'  # Белый для остальных символов (например, пробел)


def text_to_image(text, square_size=20, dpi=300):
    lines = text.split('\n')
    width = max(len(line) for line in lines)
    height = len(lines)

    # Создание пустого изображения
    img_width = width * square_size
    img_height = height * square_size
    image = Image.new('RGB', (img_width, img_height), color='#FFFFFF')
    draw = ImageDraw.Draw(image)

    # Рисование квадратов
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            color = get_color(char)
            draw.rectangle(
                [x * square_size, y * square_size, (x + 1) * square_size, (y + 1) * square_size],
                fill=color
            )

    # Сохранение изображения с разрешением 300 dpi
    image.save('poem_image.png', dpi=(dpi, dpi))


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


file_path = './task3/idiot.txt'
text = read_file(file_path)
# Преобразование текста в изображение
text_to_image(text)
