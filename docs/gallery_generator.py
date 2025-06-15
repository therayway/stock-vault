import os
from urllib.parse import quote_plus
from PIL import Image

IMAGE_DIR = "docs/images"
THUMB_DIR = "docs/images/thumbs"
OUTPUT_FILE = "docs/index.html"
AFFILIATE_TEMPLATE = "https://example.com/product?ref=ai&img={}"

CSS = """
<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #0d0d0d;
    color: #eee;
    margin: 2rem;
    line-height: 1.6;
  }
  h1 {
    text-align: center;
    color: #00ffe0;
  }
  .buttons {
    text-align: center;
    margin: 2rem auto;
  }
  .buttons a {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    margin: 0.5rem;
    background: #222;
    color: #fff;
    text-decoration: none;
    font-weight: bold;
    border-radius: 6px;
    transition: background 0.2s ease;
  }
  .buttons a:hover {
    background: #444;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 2rem;
  }
  .grid figure {
    margin: 0;
    text-align: center;
  }
  .grid img {
    width: 100%;
    border-radius: 6px;
    box-shadow: 0 0 8px rgba(0,0,0,0.4);
  }
  figcaption {
    color: #aaa;
    font-size: 0.9rem;
    margin-top: 0.5rem;
  }
  .placeholder {
    text-align: center;
    font-style: italic;
    color: #aaa;
    border: 1px dashed #333;
    padding: 2rem;
    margin-top: 3rem;
    background: #1a1a1a;
    border-radius: 8px;
  }
</style>
"""

def generate_thumbnails():
    os.makedirs(THUMB_DIR, exist_ok=True)
    for filename in os.listdir(IMAGE_DIR):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            full_path = os.path.join(IMAGE_DIR, filename)
            thumb_path = os.path.join(THUMB_DIR, filename)
            if not os.path.exists(thumb_path):
                with Image.open(full_path) as img:
                    img.thumbnail((300, 300))
                    img.save(thumb_path)
                    print(f"🖼 Created thumbnail for {filename}")

def generate():
    print("🧠 Generating gallery...")

    os.makedirs(IMAGE_DIR, exist_ok=True)
    generate_thumbnails()

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
        print(f"📁 Created missing image directory: {IMAGE_DIR}")

    files = sorted(f for f in os.listdir(IMAGE_DIR)
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')))

    print(f"📦 Found {len(files)} image(s) in {IMAGE_DIR}")

    with open(OUTPUT_FILE, 'w') as out:
        out.write("<!DOCTYPE html><html><head>\n")
        out.write("<meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1'>\n")
        out.write("<title>AI-Generated Stock Vault</title>\n")
        out.write(CSS)
        out.write("</head><body>\n")
        out.write("<h1>AI-Generated Stock Vault</h1>\n")

        out.write("""
        <div class="buttons">
          <a href="https://gumroad.com/l/urbanpack" target="_blank">📦 Buy the Unwatermarked HD Pack</a>
          <a href="https://therayway.substack.com" target="_blank">✉️ Get Premium Drops via Substack</a>
        </div>
        """)

        if files:
            out.write("<div class='grid'>\n")
            for fn in files:
                alt = os.path.splitext(fn)[0].replace("-", " ").replace("_", " ")
                link = AFFILIATE_TEMPLATE.format(quote_plus(fn))
                out.write(f"<a href='{link}' target='_blank'><img src='images/{fn}' alt='{alt}' loading='lazy'></a>\n")
            out.write("</div>\n")
        else:
            out.write("<p class='placeholder'>Gallery is under construction. Check back soon for curated AI-generated visuals.</p>\n")

        out.write("</body></html>")
        print(f"✅ Gallery written to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate()
