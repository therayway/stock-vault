import os
from urllib.parse import quote_plus

IMAGE_DIR = "docs/images"
OUTPUT_FILE = "/Volumes/stock-host/stock-vault/docs/index.html"
AFFILIATE_TEMPLATE = "https://example.com/product?ref=ai&img={}"

CSS = """
<style>
  body { font-family: sans-serif; margin: 1rem; background: #fff; color: #111; }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr)); gap: 1rem; }
  .grid img { width: 100%; height: auto; border-radius: 8px; }
  .placeholder { font-style: italic; color: #666; margin-top: 2rem; }
</style>
"""

def generate():
    files = sorted(f for f in os.listdir(IMAGE_DIR)
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')))
    with open(OUTPUT_FILE, 'w') as out:
        out.write("<!DOCTYPE html><html><head>\n")
        out.write("<meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1'>\n")
        out.write("<title>AI-Generated Stock Vault</title>\n")
        out.write(CSS + "</head><body>\n<h1>AI-Generated Stock Vault</h1>\n")

        out.write("""
        <p>
          <a href="https://gumroad.com/l/urbanpack" target="_blank"
          style="display:inline-block; padding:0.6rem 1.2rem; background:#ff6f61; color:#fff;
          text-decoration:none; font-weight:bold; border-radius:6px;">
            📦 Buy the Unwatermarked HD Pack
          </a>
        </p>
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

if __name__ == "__main__":
    os.makedirs(IMAGE_DIR, exist_ok=True)
    generate()
