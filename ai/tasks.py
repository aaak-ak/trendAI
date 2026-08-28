from celery import shared_task
from ai.services import generate_hooks, generate_captions, generate_scripts
from ai.models import Content
from product_engine.models import Product

@shared_task
def generate_ai_content(product_id):
    product = Product.objects.get(id=product_id)
    hooks = generate_hooks(product.title)
    captions = generate_captions(product.title)
    scripts = generate_scripts(product.title)

    Content.objects.create(
        product=product,
        hook="\n".join(hooks),
        caption="\n".join(captions),
        script="\n".join(scripts)
    )
