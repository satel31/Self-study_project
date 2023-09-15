# Generated by Django 4.2.5 on 2023-09-15 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_delete_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.test', verbose_name='Test'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='learning.test', verbose_name='Test'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='learning.question', verbose_name='Question'),
        ),
    ]