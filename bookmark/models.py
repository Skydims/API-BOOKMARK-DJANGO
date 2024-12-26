from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=255)  # Nama atau judul bookmark
    url = models.URLField()  # Link bookmark
    description = models.TextField(blank=True, null=True)  # Deskripsi opsional
    created_at = models.DateTimeField(auto_now_add=True)  # Tanggal dibuat

    def __str__(self):
        return self.title
