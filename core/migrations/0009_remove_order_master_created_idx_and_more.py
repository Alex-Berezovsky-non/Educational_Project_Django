# Generated by Django 5.1.7 on 2025-04-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_service_duration'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='order',
            name='master_created_idx',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='appountment_date',
            new_name='appointment_date',
        ),
        migrations.AlterField(
            model_name='master',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/masters/'),
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['client_name', 'phone', 'comment'], name='client_phone_comment_idx'),
        ),
    ]
