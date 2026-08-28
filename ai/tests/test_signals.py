import pytest
from product_engine.models import Product
from ai.models import Content

@pytest.mark.django_db
def test_content_created_on_product_save():
    # Створюємо продукт
    product = Product.objects.create(title="Test Product", price=100)

    # Перевіряємо, що контент згенерувався
    contents = Content.objects.filter(product=product)
    assert contents.exists()
    assert any(c.hook for c in contents)
