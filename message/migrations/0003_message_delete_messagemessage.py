# Generated by Django 4.2.1 on 2023-05-15 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_messagemessage_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='MessageMessage',
        ),
    ]