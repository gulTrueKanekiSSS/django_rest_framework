import os

import stripe

from users.models import Payments

stripe.api_key = ""

def get_pay(amount_payment, user):
    stripe.api_key = os.getenv("STRIPE_API_KEY")

    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount_payment,
            currency="usd",
            payment_method_types=["card"]
        )

        payment = Payments.objects.create(
            user=user,
            sum_of_pay=amount_payment,
            stripe_id=payment_intent.id
        )

        return payment
    except stripe.error.StripeError as e:
        print(f"Произошла ошибка при создании платежа: {e}")
        return None