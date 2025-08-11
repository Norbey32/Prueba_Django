from app.core.models import Type

# Create your tests here.

new_type = Type()
new_name = "Contador"
new_type.save()


Type.objects.all()