from PIL import Image


def my_replace(path:str):
    image = Image.open(path)
    image = image.convert('RGB')
    new_image = Image.new('RGB', image.size)

    for x in range(image.width):
        for y in range(image.height):
            color = image.getpixel((x, y))
            if color == (255,255,255):
                new_image.putpixel((x, y), (101,205,170))
            else:
                new_image.putpixel((x, y), color)

    new_image.save('my_img.png')


def my_findcolor(path:str):
    image = Image.open(path)
    image = image.convert('RGB')

    load = list()

    for x in range(image.width):
        for y in range(image.height):
            color = image.getpixel((x, y))
            if color in load:
                pass
            else:
                load.append(color)
    print(load)


# my_findcolor('my_img.png')
my_replace('head.png')

