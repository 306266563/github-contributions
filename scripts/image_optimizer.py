import os
from PIL import Image

def optimize_images(directory, quality=85):
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            img = Image.open(filepath)
            img.save(filepath, quality=quality, optimize=True)
            print(f"Optimized {filename}")

if __name__ == "__main__":
    # Example usage
    # optimize_images('./images')
    pass

# Minor update 1 at 2026-06-01T13:48:43
# Minor update 2 at 2026-06-01T16:24:43
# Minor update 3 at 2026-06-01T12:05:43
# Minor update 4 at 2026-06-01T18:44:43
# Minor update 5 at 2026-06-01T16:40:43
# Minor update 6 at 2026-06-01T13:49:43
# Minor update 7 at 2026-06-01T12:48:43