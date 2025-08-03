from PIL import Image, ImageDraw, ImageFont
import random

# Config
WIDTH = 140           # wider width
HEIGHT = 35           # rows
DIGIT_FONT_SIZE = 24  # font size for digits
MESSAGE_FONT_SIZE = 80 # bigger font size for message
FRAMES = 120          # total frames (~12 seconds at 100ms)
MESSAGE = """I'm watching you 
            Don't look away"""  # message to display
MESSAGE_DURATION_FRAMES = 15  # message visible for 1.5 seconds

BINARY_CHARS = ['0', '1']

# Load fonts separately for digits and message
try:
    DIGIT_FONT = ImageFont.truetype("DejaVuSansMono.ttf", DIGIT_FONT_SIZE)
    MESSAGE_FONT = ImageFont.truetype("DejaVuSansMono.ttf", MESSAGE_FONT_SIZE)
except:
    DIGIT_FONT = ImageFont.load_default()
    MESSAGE_FONT = ImageFont.load_default()

def init_columns():
    return [[random.choice(BINARY_CHARS) for _ in range(HEIGHT)] for _ in range(WIDTH)]

def update_columns(columns):
    for col in columns:
        col.pop()
        col.insert(0, random.choice(BINARY_CHARS))

def draw_rain_frame(columns):
    img_width = WIDTH * DIGIT_FONT_SIZE // 2
    img_height = HEIGHT * DIGIT_FONT_SIZE
    image = Image.new("RGB", (img_width, img_height), "black")
    draw = ImageDraw.Draw(image)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            px = x * DIGIT_FONT_SIZE // 2
            py = y * DIGIT_FONT_SIZE
            char = columns[x][y]
            draw.text((px, py), char, font=DIGIT_FONT, fill=(0, 255, 0))
    return image

def draw_message_frame():
    img_width = WIDTH * DIGIT_FONT_SIZE // 2
    img_height = HEIGHT * DIGIT_FONT_SIZE
    image = Image.new("RGB", (img_width, img_height), "black")
    draw = ImageDraw.Draw(image)

    bbox = MESSAGE_FONT.getbbox(MESSAGE)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (img_width - text_width) // 2
    y = (img_height - text_height) // 2

    draw.text((x, y), MESSAGE, font=MESSAGE_FONT, fill=(144, 238, 144))  # Light green
    return image

def generate_gif(output_path="matrix_wide_message.gif"):
    columns = init_columns()
    frames = []

    for frame_idx in range(FRAMES):
        cycle = MESSAGE_DURATION_FRAMES * 6  # longer cycles
        frame_in_cycle = frame_idx % cycle
        if frame_in_cycle < MESSAGE_DURATION_FRAMES:
            frames.append(draw_message_frame())
        else:
            frames.append(draw_rain_frame(columns))
            update_columns(columns)

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=80, loop=0)
    print(f"Saved wide matrix rain with message GIF: {output_path}")

if __name__ == "__main__":
    generate_gif()
