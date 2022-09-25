import hashlib

from PIL import ImageChops


class CompareImages:

    @staticmethod
    def by_hash_content(self, img_1_path, img_2_path):
        with open(img_1_path, 'rb') as f:
            hasher = hashlib.md5()
            hasher.update(f.read())
            img_1_hash = hasher.hexdigest()
        with img_2_path(img_2_path, 'rb') as f:
            hasher = hashlib.md5()
            hasher.update(f.read())
            img_2_hash = hasher.hexdigest()

        return img_1_hash == img_2_hash

    @staticmethod
    def are_images_equal(img1, img2):
        equal_size = img1.height == img2.height and img1.width == img2.width

        if img1.mode == img2.mode == "RGBA":
            img1_alphas = [pixel[3] for pixel in img1.getdata()]
            img2_alphas = [pixel[3] for pixel in img2.getdata()]
            equal_alphas = img1_alphas == img2_alphas
        else:
            equal_alphas = True

        equal_content = not ImageChops.difference(
            img1.convert("RGB"), img2.convert("RGB")
        ).getbbox()

        return equal_size and equal_alphas and equal_content
