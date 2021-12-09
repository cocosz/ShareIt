# Generated by Django 3.2.6 on 2021-09-16 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datacontrol', '0011_auto_20210916_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlog',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_order_logs', to='datacontrol.studentprofile'),
        ),
        migrations.AlterField(
            model_name='orderlog',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_order_logs', to='datacontrol.shopprofile'),
        ),
    ]
