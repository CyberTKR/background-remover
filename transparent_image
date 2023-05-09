from PIL import Image


class TransparentImage:
    def __init__(self, image_path):
        self.image_path = image_path

    def make_transparent(self, save_path):
        with Image.open(self.image_path) as img:
            img = img.convert("RGBA")
            data = img.getdata()

            # Set alpha values for all pixels.
            new_data = []
            for item in data:
                if sum(item[:3]) > 600:
                    new_data.append(item[:3] + (30,))
                else:
                    new_data.append(item[:3] + (255,))

            # Save the new image.
            img.putdata(new_data)
            img.save(save_path)
