# Generated by Django 3.0.8 on 2020-07-17 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("peering", "0059_router_last_deployment_id")]

    operations = [
        migrations.AlterField(
            model_name="router",
            name="napalm_password",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="router",
            name="napalm_username",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
