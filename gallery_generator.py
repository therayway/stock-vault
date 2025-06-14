# gallery_generator.py
import os
from urllib.parse import quote_plus

# CONFIG
IMAGE_DIR = "images"
OUTPUT_FILE = "index.html"
AFFILIATE_URL = "https://example.com/product?ref=ai&img={}"

# Inline CSS for a responsive grid
CSS = """
<style>
  body { font-family: sans-serif; margin: 0; padding: 1rem; }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr)); gap: 1rem; }
  .grid a { display: block; }
  .grid img { width: 100%; height: auto; display: block; border-radius: 4px; }
</style>
"""

def make_index():
    files = sorted(f for f in os.listdir(IMAGE_DIR)
                   if f.lower().endswith(('.jpg','.jpeg','.png','.gif')))
    with open(OUTPUT_FILE, 'w') as out:
        out.write(f"<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
        out.write("  <meta charset='utf-8'>\n")
        out.write("  <meta name='viewport' content='width=device-width,initial-scale=1'>\n")
        out.write("  <title>AI Image Gallery</title>\n")
        out.write(f"{CSS}\n</head>\n<body>\n")
        out.write("  <h1>AI-Generated Stock Vault</h1>\n")
        out.write("  <div class='grid'>\n")
        for fn in files:
            url = AFFILIATE_URL.format(quote_plus(fn))
            src = f"{IMAGE_DIR}/{quote_plus(fn)}"
            alt = os.path.splitext(fn)[0].replace('-', ' ').replace('_',' ')
            out.write(f"    <a href='{url}' target='_blank'>\n")
            out.write(f"      <img src='{src}' alt='{alt}' loading='lazy'>\n")
            out.write("    </a>\n")
        out.write("  </div>\n</body>\n</html>")

if __name__ == "__main__":
    os.makedirs(IMAGE_DIR, exist_ok=True)
    make_index()
