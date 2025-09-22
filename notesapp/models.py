from django.db import models

class Note(models.Model):

    CATEGORY = (('WORK','Work'),
                ('PERSONAL','Personal'),
                ('IMPORTANT','Important'))


    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(unique = True)
    category = models.CharField(max_length = 15, choices=CATEGORY, default="PERSONAL")
    created = models.DatesTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        """
        Generate a unique slug from the title on first save.
        """
        if not self.slug:
            slug_base = slugify(self.title)
            slug = slug_base
            if Note.objects.filter(slug=slug).exists():
                slug = f'{slug_base}-{get_random_string(5)}'
            self.slug = slug
        super(Note, self).save(*args, **kwargs)
