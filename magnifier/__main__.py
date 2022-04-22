from PIL import Image
from pathlib import Path
import sys


try:
    input_arg = sys.argv[1]
except IndexError:
    print('input path missing')
    print('> python magnifier path/to/images/')
    sys.exit(1)

input_dir = Path(sys.argv[1])
output_dir = input_dir.joinpath('resized')
output_dir.mkdir(exist_ok=True)


def get_new_dimensions(x, y):
    # for 8.5 x 11, 2550+ x 3300+ pixels
    # https://www.docucopies.com/image-resolution/
    x_ideal = 2550
    y_ideal = 3300
    ratio = min(x_ideal / x, y_ideal / y)
    return (int(x * ratio), int(y * ratio))

def resize(img_path):
    image = Image.open(img_path)
    x, y = image.size
    new_dimensions = get_new_dimensions(x, y)
    resized_name = output_dir.joinpath(img_path.name)
    print(f'{img_path}, ({x}, {y}) -> {resized_name} {new_dimensions}')
    resized_image = image.resize(new_dimensions)
    resized_image.save(resized_name, optimize=True, quality=100)


extensions = ['.png', '.jpg', '.jpeg']
for x in input_dir.iterdir():
    if x.is_file() and x.suffix.lower() in extensions:
        name = x.name
        resize(x)
