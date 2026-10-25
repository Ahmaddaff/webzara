from PIL import Image
import os

src_dir = r"C:\Users\Thinkpad X13\WorkBuddy AI\2026-10-26-02-12-53\images"
out_dir = r"C:\Users\Thinkpad X13\WorkBuddy AI\2026-10-26-02-12-53\images_opt"
os.makedirs(out_dir, exist_ok=True)

max_size = (800, 800)

for i in range(1, 11):
    fname = f"{i}.png"
    src_path = os.path.join(src_dir, fname)
    out_path = os.path.join(out_dir, f"{i}.png")
    
    img = Image.open(src_path)
    img = img.convert("RGBA")
    img.thumbnail(max_size, Image.LANCZOS)
    img.save(out_path, "PNG", optimize=True)
    
    orig_size = os.path.getsize(src_path) / 1024
    new_size = os.path.getsize(out_path) / 1024
    print(f"{fname}: {orig_size:.0f} KB -> {new_size:.0f} KB")

print("Done!")
