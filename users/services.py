import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_stripe_product(course_name: str):
    return stripe.Product.create(name=course_name)

def create_stripe_price(product_id: str, amount: float):
    return stripe.Price.create(product=product_id, unit_amount=int(amount * 100), currency="rub")

def create_stripe_session(price_id: str, success_url: str, cancel_url: str):
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{'price': price_id, 'quantity': 1}],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )
