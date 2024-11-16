# Generated by Django 5.1.1 on 2024-10-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_gallery_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='V_Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(default='default.mov', upload_to='GVD/%Y/%m/%d')),
                ('demo_link', models.CharField(blank=True, max_length=200)),
                ('source_link', models.CharField(blank=True, max_length=200)),
                ('vote_total', models.IntegerField(blank=True, default=0)),
                ('vote_ratio', models.IntegerField(blank=True, default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, to='gallery.album')),
            ],
        ),
    ]