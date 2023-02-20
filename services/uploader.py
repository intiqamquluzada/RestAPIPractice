class Uploader:

    @staticmethod
    def upload_images(instance, filename):
        return f"photo/{instance.slug}/{filename}"