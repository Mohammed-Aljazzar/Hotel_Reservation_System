from django.db import migrations, models
from django.utils.text import slugify


def populate_category_slugs(apps, schema_editor):
    Category = apps.get_model("blog", "Category")
    TranslatableField = apps.get_model("tof", "TranslatableField")
    Translation = apps.get_model("tof", "Translation")

    name_field = TranslatableField.objects.filter(
        content_type__app_label="blog",
        content_type__model="category",
        name="name",
    ).first()

    for category in Category.objects.all():
        value = category.name
        if not value and name_field:
            translations = Translation.objects.filter(field=name_field, object_id=category.pk)
            value = (
                translations.filter(lang_id="en").values_list("value", flat=True).first()
                or translations.values_list("value", flat=True).first()
            )
        base_slug = slugify(value, allow_unicode=True) or f"category-{category.pk}"
        slug = base_slug
        index = 2
        while Category.objects.exclude(pk=category.pk).filter(slug=slug).exists():
            slug = f"{base_slug}-{index}"
            index += 1
        category.slug = slug
        category.save(update_fields=["slug"])


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_translate_blog_admin_labels"),
        ("tof", "0004_alter_translatablefield_id_alter_translation_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=80, null=True),
        ),
        migrations.RunPython(populate_category_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=80, unique=True),
        ),
    ]
