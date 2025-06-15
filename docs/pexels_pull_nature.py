import os
import requests
import re

API_KEY = "pPoEztx1EzTC1Qw5XZm0m3V57mW06Qsn9utVAnYrNXDJqTQX9gVbVTMm"
QUERY = "nature landscapes"
IMAGE_COUNT = 10
OUTPUT_DIR = "docs/images"

os.makedirs(OUTPUT_DIR, exist_ok=True)

headers = {
    "Authorization": API_KEY
}

params = {
    "query": QUERY,
    "per_page": IMAGE_COUNT
}

print(f"📥 Searching Pexels for: {QUERY}")
response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    if data["photos"]:
        metadata_list = []
        for i, photo in enumerate(data["photos"], 1):
            alt = photo["alt"].lower().strip().replace(" ", "-")
            url = photo["src"]["original"]
            clean_filename = re.sub(r'[^a-z0-9\-]', '', alt)[:40]
            filename = f"{i:02d}-{clean_filename}.jpg"
            path = os.path.join(OUTPUT_DIR, filename)

            img = requests.get(url)
            if img.status_code == 200:
                with open(path, "wb") as f:
                    f.write(img.content)
                print(f"✅ {filename}")
                metadata_list.append({
                    "filename": filename,
                    "caption": photo["alt"],
                    "photographer": photo["photographer"],
                    "pexels_url": photo["url"]
                })
            else:
                print(f"⚠️ Failed to download: {url}")

        # Save metadata as captions or description
        with open("nature_captions.txt", "w") as f:
            for meta in metadata_list:
                f.write(f"- [{meta['caption']}]({meta['pexels_url']}) by {meta['photographer']}\n")
        print("📝 Saved metadata to nature_captions.txt")
    else:
        print("❌ No images found for this query.")
else:
    print(f"❌ API request failed: {response.status_code}")
