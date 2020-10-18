import stripe
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from .models import Orders,Address
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_API_KEY_SECRET

@login_required
def payment(request):
    return render(request,'stripe.html')

@login_required
def get_session(request):
    if request.is_secure():
        DOMAIN = f'https://{request.META["HTTP_HOST"]}/'
    else:
        DOMAIN = f'http://{request.META["HTTP_HOST"]}/'
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'gbp',
                    'unit_amount': int(round(request.user.get_cart_total,2)*100),
                    'product_data': {
                    'name': 'Stubborn Attachments',
                    },
                },
                'quantity': 1
            },
        ],
        mode='payment',
        success_url=DOMAIN + 'success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=DOMAIN + 'cancel',
    )
    return JsonResponse({'id':checkout_session.id})

@login_required
def success(request):
    id = request.GET.get('session_id')
    checkout_session = stripe.checkout.Session.retrieve(id)
    obj = Orders.objects.create(customer_id=checkout_session['customer'],stripe_id=checkout_session['id'],user=request.user,address=Address.objects.get(pk=int(request.session['address'])))

    return redirect('home')
