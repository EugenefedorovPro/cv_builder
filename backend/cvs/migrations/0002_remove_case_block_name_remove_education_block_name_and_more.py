# Generated by Django 5.2.1 on 2025-06-12 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cvs", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="case",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="education",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="experience",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="feedback",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="hardskill",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="header",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="interest",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="manifest",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="naturallanguage",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="photos",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="project",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="softskill",
            name="block_name",
        ),
        migrations.RemoveField(
            model_name="whyme",
            name="block_name",
        ),
    ]
