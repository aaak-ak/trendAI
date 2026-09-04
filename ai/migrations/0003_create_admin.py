from django.db import migrations

def create_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )

class Migration(migrations.Migration):

    dependencies = [
    ('ai', '0002_alter_content_options_content_trend_and_more'),
]

    operations = [
        migrations.RunPython(create_admin),
    ]
