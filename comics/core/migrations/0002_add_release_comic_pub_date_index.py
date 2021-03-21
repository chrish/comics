# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="release",
            index=models.Index(
                fields=[b"comic", b"pub_date"],
                name="comics_rele_comic_i_2b6b41_idx",
            ),
        ),
    ]