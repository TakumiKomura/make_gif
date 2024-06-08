from PIL import Image, ImageDraw, ImageFont, ImageSequence
import numpy as np

# Load the existing GIF
input_path = "pics3465.gif"
original_gif = Image.open(input_path)

# Function to add the specified sparkle effect
def add_sparkle_effect(frame):
    draw = ImageDraw.Draw(frame)
    width, height = frame.size

    # Draw yellow circles (sparkles) at random positions
    for _ in range(30):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        radius = np.random.randint(1, 4)
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill="yellow")

    return frame

# Load the correct font for Japanese characters
font_path = "NotoSansCJKjp-Regular.otf"

# Function to add text using a specific font that supports Japanese characters
def add_text(frame, text, y, font_size=10):
    draw = ImageDraw.Draw(frame)
    font = ImageFont.truetype(font_path, font_size)
    
    # Split text by newline characters
    lines = text.split('\n')
    line_height = font.getsize("A")[1]
    
    for line in lines:
        text_width = font.getsize(line)[0]
        x = (frame.width - text_width) // 2
        draw.text((x, y), line, font=font, fill="red")
        y += line_height
    
    return frame

# Process each frame again with the updated sparkle effect function
frames = []
names = input("input names :")
for frame in ImageSequence.Iterator(original_gif):
    frame = frame.convert("RGBA")
    frame = add_sparkle_effect(frame)
    frame = add_text(frame, names, y=10, font_size=10)
    frame = add_text(frame, "皆\n勤\n賞", y=40, font_size=20)
    frames.append(frame)

# Save the modified GIF
output_path = "kaikin_award.gif"
frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=original_gif.info['duration'])
