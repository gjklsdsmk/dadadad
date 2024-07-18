from PIL import Image, ImageDraw, ImageFont
from config import bot_username

LabelFont = ImageFont.truetype("font.otf", size=230)
TextFont = ImageFont.truetype("font.otf", size=100)
WaterFont = ImageFont.truetype("font.otf", size=50)
win_color_hex, draw_color_hex, lose_color_hex, text_color_hex = "#00fa9a", "#e0d845", "#ff7070", "#0f0f0f"



def create_win_photo(name, summ, win_summ):
    im = Image.new('RGB', (1600,900), color=(win_color_hex))
    imd = ImageDraw.Draw(im)
    if len(name) > 10:
        name = f"{name[:11]}..."
    imd.text((300, 70), "Победа)", font=LabelFont, fill=text_color_hex, align="center")
    imd.text((150, 400), f"Игрок: {name}\nСумма ставки: {summ}$\nСумма выигрыша: {win_summ}$", font=TextFont, fill=text_color_hex)
    imd.text((630, 850), f'@{bot_username}', font=WaterFont, fill=text_color_hex)
    return im


def create_lose_photo(name, summ):
    im = Image.new('RGB', (1600,900), color=(lose_color_hex))
    imd = ImageDraw.Draw(im)
    if len(name) > 10:
        name = f"{name[:11]}..."
    imd.text((108, 70), "Поражение(", font=LabelFont, fill=text_color_hex, align="center")
    imd.text((150, 400), f"Игрок: {name}\nСумма ставки: {summ}$\nУдачи в следующей игре", font=TextFont, fill=text_color_hex)
    imd.text((630, 850), f'@{bot_username}', font=WaterFont, fill=text_color_hex)
    return im


def create_draw_photo(name, summ):
    im = Image.new('RGB', (1600,900), color=(draw_color_hex))
    imd = ImageDraw.Draw(im)
    if len(name) > 10:
        name = f"{name[:11]}..."
    imd.text((170, 70), "Ничья -_-", font=LabelFont, fill=text_color_hex, align="center")
    imd.text((150, 400), f"Игрок: {name}\nСумма ставки: {summ}$\nВерните ставку по\nссылке ниже", font=TextFont, fill=text_color_hex)
    imd.text((630, 850), f'@{bot_username}', font=WaterFont, fill=text_color_hex)
    return im


def create_error_photo(error_text):
    im = Image.new('RGB', (1600,900), color=(draw_color_hex))
    imd = ImageDraw.Draw(im)
    imd.text((300, 70), "Ошибка(", font=LabelFont, fill=text_color_hex, align="center")
    imd.text((150, 370), error_text, font=TextFont, fill=text_color_hex)
    imd.text((630, 850), f'@{bot_username}', font=WaterFont, fill=text_color_hex)
    return im



if __name__ == "__main__":
    create_error_photo("Описание ошибки").show()