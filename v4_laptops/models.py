from django.db import models
# from django.contrib.auth.models import User

PROCESSOR_CHOICES = (
    ("", "----"),
    ("AMD Dual Core Ryzen", "AMD Dual Core Ryzen"),
    ("Intel Dual Core", "Intel Dual Core"),
    ("Apple M1 Chip", "Apple M1 Chip"),
    ("Intel 8 Core", "Intel 8 Core"),
    ("Core i3", "Core i3"),
    ("Core i5", "Core i5"),
    ("Core i7", "Core i7"),
    ("Core i10", "Core i10"),
)

COLOR_CHOICES = (
    ("", "----"),
    ("Black", "Black"),
    ("Gray", "Gray"),
    ("Space Grey", "Space Grey"),
    ("White", "White"),
    ("Red", "Red"),
    ("Pink", "Pink"),
    ("Denium Blue", "Denium Blue"),
    )


# Create class Laptop
class V4_Laptop(models.Model):
    stored = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=50, blank=True, default='')
    model = models.CharField(max_length=50)
    ssd = models.BooleanField(default=False)
    processor = models.CharField(choices=PROCESSOR_CHOICES, default=None, max_length=50)
    color = models.CharField(choices=COLOR_CHOICES, default=None, max_length=50)
    owner = models.ForeignKey('auth.User', related_name='v4_laptops', on_delete=models.CASCADE)

    class Meta:
        ordering = ['stored']

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
