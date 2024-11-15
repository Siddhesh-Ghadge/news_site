# Generated by Django 5.0.7 on 2024-11-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(blank=True, max_length=100)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]