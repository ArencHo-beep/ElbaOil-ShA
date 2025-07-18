from PIL import Image, ImageDraw, ImageFont

# Image settings
width, height = 400, 100
background_color = (255, 255, 255)
text_color = (0, 83, 156)
highlight_color = (229, 57, 53)

# Create a new image with white background
img = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(img)

# Load font
try:
    font = ImageFont.truetype("arialbd.ttf", 60)
except IOError:
    font = ImageFont.load_default()

# Draw "ELBA IL" with space for the "O"
text = "ELBA IL"
text_x, text_y = 20, 20
draw.text((text_x, text_y), text, font=font, fill=text_color)

# Position the red circle "O"
o_x_offset = draw.textlength("ELBA ", font=font)
circle_radius = 25
circle_center = (text_x + int(o_x_offset) + circle_radius, text_y + 5 + circle_radius)

# Draw the red circle
draw.ellipse(
    [
        (circle_center[0] - circle_radius, circle_center[1] - circle_radius),
        (circle_center[0] + circle_radius, circle_center[1] + circle_radius)
    ],
    fill=highlight_color
)

# Save the image
img.save("elbaoil_logo.png")
print("✅ Saved 'elbaoil_logo.png'")
