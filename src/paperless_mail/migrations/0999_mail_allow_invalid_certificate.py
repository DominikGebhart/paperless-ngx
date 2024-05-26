from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("paperless_mail", "0023_remove_mailrule_filter_attachment_filename_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="MailAccount",
            name="imap_security",
            field=models.PositiveIntegerField(
                choices=[
                            (1, "No encryption"),
                            (2, "Use SSL"),
                            (3, "Use STARTTLS"),
                            (4, "Use SSL, no host check"),
                            (5, "Use STARTTLS, no host check"),
                            (6, "Use SSL, allow invalid certificate"),
                            (7, "Use STARTTLS, allow invalid certificate"),
                        ],
                default=2,
                verbose_name="IMAP security",
            ),
        ),
    ]
