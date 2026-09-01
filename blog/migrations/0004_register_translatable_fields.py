from django.db import migrations


TRANSLATABLE_FIELDS = {
    "category": (("name", "Name"),),
    "post": (
        ("title", "Title"),
        ("description", "Description"),
    ),
}


def register_fields_and_existing_values(apps, schema_editor):
    ContentType = apps.get_model("contenttypes", "ContentType")
    Language = apps.get_model("tof", "Language")
    TranslatableField = apps.get_model("tof", "TranslatableField")
    Translation = apps.get_model("tof", "Translation")

    # The translation selector requires language rows.  Arabic and English
    # match the languages configured by the project.
    for iso in ("ar", "en"):
        Language.objects.get_or_create(iso=iso, defaults={"is_active": True})

    for model_name, fields in TRANSLATABLE_FIELDS.items():
        Model = apps.get_model("blog", model_name.title())
        content_type, _ = ContentType.objects.get_or_create(
            app_label="blog",
            model=model_name,
        )
        for field_name, title in fields:
            field, _ = TranslatableField.objects.get_or_create(
                content_type=content_type,
                name=field_name,
                defaults={"title": title},
            )

            # Preserve the existing content as the English translation.
            for obj in Model.objects.exclude(**{field_name: ""}):
                Translation.objects.get_or_create(
                    content_type=content_type,
                    object_id=obj.pk,
                    field=field,
                    lang_id="en",
                    defaults={"value": getattr(obj, field_name)},
                )


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_translation_labels"),
        ("tof", "0004_alter_translatablefield_id_alter_translation_id"),
    ]

    operations = [
        migrations.RunPython(register_fields_and_existing_values, migrations.RunPython.noop),
    ]
