from os.path import dirname, join
from random import randint

from PIL import Image, ImageDraw, ImageFont


ttf_path = join(dirname(__file__), 'ttf', 'Vera.ttf')
welcome_size = 164, 314
header_size = 150, 57
icon_size = 256, 256
bg = 0x33, 0x66, 0x99
white = 0xff, 0xff, 0xff


def new_background(size, color, bs=20, boxes=50):
    im = Image.new('RGB', size, color=color)
    d = ImageDraw.Draw(im)
    for unused in range(boxes):
        x0 = randint(0, size[0] - bs)
        y0 = randint(0, size[1] - bs)
        c = tuple(randint(v - 10, v + 10) for v in color)
        d.rectangle((x0, y0, x0 + bs, y0 + bs), fill=c)
    return im


def welcome_image(name, version):
    font = ImageFont.truetype(ttf_path, 20)
    im = new_background(welcome_size, bg)
    d = ImageDraw.Draw(im)
    d.text((20, 100), name, fill=white, font=font)
    d.text((20, 130), version, fill=white, font=font)
    return im


def header_image(name, unused=None):
    font = ImageFont.truetype(ttf_path, 20)
    im = new_background(header_size, bg)
    d = ImageDraw.Draw(im)
    d.text((20, 15), name, fill=white, font=font)
    return im


def icon_image(name, unused=None):
    font = ImageFont.truetype(ttf_path, 200)
    im = new_background(icon_size, bg)
    d = ImageDraw.Draw(im)
    d.text((60, 20), name[0], fill=white, font=font)
    return im


def write_images(info, dir_path):
    for tp, size, f, ext in [
        ('welcome', welcome_size, welcome_image, '.bmp'),
        ('header',  header_size,  header_image,  '.bmp'),
        ('icon',    icon_size,    icon_image,    '.ico')
        ]:
        key = tp + '_image'
        if key in info:
            im = Image.open(info[key])
            im = im.resize(size)
        else:
            im = f(info['name'], info['version'])
        assert im.size == size
        im.save(join(dir_path, tp + ext))


if __name__ == '__main__':
    info = {'name': 'test', 'version': '0.3.1',
            'welcome_image': '/Users/ilan/Desktop/moit.png'}
    write_images(info, 'tmp')