#!/usr/bin/env python3
"""
generate_branding_assets.py

Processes SnappGridLogo.jpg to generate all brand icon assets and Open Graph banner:
- favicon.ico (16x16, 32x32, 48x48)
- favicon-32x32.png
- favicon-16x16.png
- apple-touch-icon.png (180x180)
- android-chrome-192x192.png
- android-chrome-512x512.png
- og-image.jpg (1200x630)
"""

import os
from PIL import Image
import numpy as np

def generate_branding():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logo_path = os.path.join(base_dir, 'SnappGridLogo.jpg')

    if not os.path.exists(logo_path):
        raise FileNotFoundError(f"Logo not found at {logo_path}")

    img = Image.open(logo_path)
    print(f"Loaded master logo: {img.size} {img.format} {img.mode}")

    # 1. Emblem crop with elegant margin
    # Emblem true bounding box is (651, 120, 1207, 676) [556x556]
    # Adding 28px padding creates a 612x612 square with ~4.5% breathing room,
    # protecting the gold grid corners from being clipped by iOS squircles / Android circles.
    pad = 28
    crop_box = (651 - pad, 120 - pad, 1207 + pad, 676 + pad)
    emblem = img.crop(crop_box)
    print(f"Emblem crop size: {emblem.size}")

    # Export icons
    # - favicon.ico (multi-size: 16, 32, 48)
    ico_img = emblem.resize((48, 48), Image.Resampling.LANCZOS)
    favicon_ico_path = os.path.join(base_dir, 'favicon.ico')
    ico_img.save(favicon_ico_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"Exported: {favicon_ico_path}")

    # - favicon-32x32.png
    f32_path = os.path.join(base_dir, 'favicon-32x32.png')
    emblem.resize((32, 32), Image.Resampling.LANCZOS).save(f32_path, format='PNG')
    print(f"Exported: {f32_path}")

    # - favicon-16x16.png
    f16_path = os.path.join(base_dir, 'favicon-16x16.png')
    emblem.resize((16, 16), Image.Resampling.LANCZOS).save(f16_path, format='PNG')
    print(f"Exported: {f16_path}")

    # - apple-touch-icon.png (180x180)
    apple_path = os.path.join(base_dir, 'apple-touch-icon.png')
    emblem.resize((180, 180), Image.Resampling.LANCZOS).save(apple_path, format='PNG')
    print(f"Exported: {apple_path}")

    # - android-chrome-192x192.png
    a192_path = os.path.join(base_dir, 'android-chrome-192x192.png')
    emblem.resize((192, 192), Image.Resampling.LANCZOS).save(a192_path, format='PNG')
    print(f"Exported: {a192_path}")

    # - android-chrome-512x512.png
    a512_path = os.path.join(base_dir, 'android-chrome-512x512.png')
    emblem.resize((512, 512), Image.Resampling.LANCZOS).save(a512_path, format='PNG')
    print(f"Exported: {a512_path}")

    # 2. Open Graph banner og-image.jpg (1200x630)
    # The original image is 1907x1232.
    # Content center is cx = 928.5, cy = 607.
    # At aspect ratio 1200:630, height 1232 corresponds to width = 2347.
    # Target center is 2347 / 2 = 1173.5.
    # We extend the seamless dark slate textured background:
    # 245px on the left, 195px on the right using the pure slate background strips.
    arr = np.array(img)
    h, w, _ = arr.shape # 1232, 1907, 3
    target_w = int(round(h * 1200 / 630)) # 2347
    needed_left = int(round(target_w / 2 - 928.5)) # 245
    needed_right = target_w - w - needed_left # 195

    # Pure background strips (free of text/emblem)
    strip_l = arr[:, 0:120, :]
    ext_l = np.concatenate([strip_l, np.fliplr(strip_l), strip_l, np.fliplr(strip_l)], axis=1)
    left_patch = ext_l[:, -needed_left:, :]

    strip_r = arr[:, 1787:1907, :]
    ext_r = np.concatenate([np.fliplr(strip_r), strip_r, np.fliplr(strip_r), strip_r], axis=1)
    right_patch = ext_r[:, :needed_right, :]

    full_wide = np.concatenate([left_patch, arr, right_patch], axis=1)
    og_img = Image.fromarray(full_wide).resize((1200, 630), Image.Resampling.LANCZOS)
    og_path = os.path.join(base_dir, 'og-image.jpg')
    og_img.save(og_path, format='JPEG', quality=95)
    print(f"Exported: {og_path} (1200x630)")

if __name__ == '__main__':
    generate_branding()
