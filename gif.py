from PIL import Image, ImageDraw, ImageFont
import random
import os

# Constants
WIDTH = 60
HEIGHT = 20
FONT_SIZE = 16
FRAMES = 40
BINARY_CHARS = ['0', '1']
MESSAGE = "I'm watching you"

# Setup font (adjust if your system doesn't have DejaVuSansMono)
try:
    FONT = ImageFont.truetype("DejaVuSansMono.ttf", FONT_SIZE)
except IOError:
    FONT = ImageFont.load_default()

def create_frame(columns):
    img_width = WIDTH * FONT_SIZE // 2
    img_height = HEIGHT * FONT_SIZE
    image = Image.new("RGB", (img_width, img_height), color="black")
    draw = ImageDraw.Draw(image)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            msg_start = (WIDTH - len(MESSAGE)) // 2
            if y == HEIGHT // 2 and msg_start <= x < msg_start + len(MESSAGE):
                char = MESSAGE[x - msg_start]
                color = (144, 238, 144)  # Light green
            elif columns[x] >= y:
                char = random.choice(BINARY_CHARS)
                color = (0, 255, 0)  # Bright green
            else:
                continue  # leave background black
            draw.text((x * FONT_SIZE // 2, y * FONT_SIZE), char, font=FONT, fill=color)

    return image

def generate_gif(output_path="f:/readme/matrix.gif"):
    frames = []
    columns = [0] * WIDTH

    for _ in range(FRAMES):
        frame = create_frame(columns)
        frames.append(frame)

        # Update column positions
        for i in range(WIDTH):
            columns[i] = columns[i] + 1 if random.random() > 0.5 else columns[i]
            if columns[i] > HEIGHT:
                columns[i] = 0

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
    print(f"✅ Saved animation to {output_path}")

if __name__ == "__main__":
    generate_gif()
