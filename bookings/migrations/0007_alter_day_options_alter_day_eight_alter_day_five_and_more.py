# Generated by Django 4.0 on 2022-01-08 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_alter_day_eight_alter_day_five_alter_day_four_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='day',
            name='eight',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eight', to='bookings.reservation', unique=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='five',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='five', to='bookings.reservation', unique=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='four',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='four', to='bookings.reservation', unique=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='one',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='one', to='bookings.reservation', unique=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='seven',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seven', to='bookings.reservation', unique=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='six',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='six', to='bookings.reservation', unique=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='three',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='three', to='bookings.reservation', unique=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='two',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='two', to='bookings.reservation', unique=True),
        ),
    ]
