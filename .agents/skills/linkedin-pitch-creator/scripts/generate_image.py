from PIL import Image, ImageDraw, ImageFont
import random
import sys
import os

def draw_robot(draw, x, y, size, color):
    draw.rectangle([x, y, x+size, y+size*0.8], fill=color, outline=(255,255,255), width=2)
    draw.ellipse([x+size*0.2, y+size*0.2, x+size*0.35, y+size*0.35], fill=(255,255,255))
    draw.ellipse([x+size*0.65, y+size*0.2, x+size*0.8, y+size*0.35], fill=(255,255,255))
    draw.line([x+size*0.3, y+size*0.6, x+size*0.7, y+size*0.6], fill=(255,255,255), width=2)

def draw_monitor(draw, x, y, size, color):
    # Screen
    draw.rectangle([x, y, x+size, y+size*0.6], fill=(30, 30, 35), outline=(150, 150, 150), width=3)
    # Stand
    draw.rectangle([x+size*0.45, y+size*0.6, x+size*0.55, y+size*0.75], fill=(100, 100, 100))
    draw.rectangle([x+size*0.3, y+size*0.75, x+size*0.7, y+size*0.8], fill=(80, 80, 80))
    # Code lines
    for i in range(6):
        w = random.randint(int(size*0.2), int(size*0.7))
        draw.line([x+10, y+10+i*12, x+10+w, y+10+i*12], fill=color, width=3)

def draw_desk(draw, y, width, color):
    draw.rectangle([0, y, width, y+40], fill=(60, 40, 30)) # Wood brown

def draw_dna(draw, x, y, size, color):
    for i in range(8):
        offset = 15 * (i % 2)
        draw.ellipse([x+offset, y+i*15, x+offset+10, y+i*15+10], fill=color)
        draw.ellipse([x+30-offset, y+i*15, x+40-offset, y+i*15+10], fill=(255,255,255))
        draw.line([x+offset+5, y+i*15+5, x+35-offset, y+i*15+5], fill=(100, 100, 100), width=1)

def generate(title, subtitle, output_path, theme="tech", color="#00ff7f"):
    width, height = 1800, 1013
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    color_rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

    base = Image.new('RGB', (width, height), (10, 25, 47))
    draw = ImageDraw.Draw(base)
    
    # Background Gradient
    for i in range(height):
        fact = i / height
        bg = (int(10 + 15*fact), int(25 + 20*fact), int(47 + 28*fact))
        draw.line([(0, i), (width, i)], fill=bg)

    random.seed(title)
    
    if theme == "tech":
        draw_desk(draw, height-150, width, (60, 40, 30))
        for i in range(3):
            draw_monitor(draw, 150 + i*500, height-450, 300, color_rgb)
    elif theme == "bio":
        for _ in range(10):
            draw_dna(draw, random.randint(0, width), random.randint(0, height), 100, color_rgb)
    else: # Default/Network
        for _ in range(12):
            draw.ellipse([random.randint(0, width), random.randint(0, height), random.randint(0, width)+20, random.randint(0, height)+20], outline=color_rgb)

    # Text Styling
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    try:
        t_font = ImageFont.truetype(font_path, 100)
        s_font = ImageFont.truetype(font_path, 50)
    except:
        t_font = s_font = ImageFont.load_default()

    def centered_text(text, font, y, fill):
        w = draw.textbbox((0, 0), text, font=font)[2]
        x = (width - w) / 2
        draw.text((x+5, y+5), text, font=font, fill=(0,0,0)) # Shadow
        draw.text((x, y), text, font=font, fill=fill)

    centered_text(title, t_font, 350, (255, 255, 255))
    centered_text(subtitle, s_font, 480, color_rgb)
    draw.line([400, 580, 1400, 580], fill=color_rgb, width=6)

    base.save(output_path, dpi=(300, 300))

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) >= 5: generate(args[0], args[1], args[2], args[3], args[4])
    elif len(args) >= 3: generate(args[0], args[1], args[2])
