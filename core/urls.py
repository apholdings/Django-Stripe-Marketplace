
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include

from .views import (
    HomeView, 
UserProductListView, 
ProductUpdateView, 
ProductDetailView, 
CreateCheckoutSessionView,
SuccessView,
stripe_webhook
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('users/', include('accounts.urls', namespace='users')),

    path('create-checkout-session/<slug>/', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
    path("success/", SuccessView.as_view(), name="success"),
    path("webhooks/stripe/", stripe_webhook, name="stripe-webhook"),


    path('', HomeView.as_view(), name="home"),
    path('products/', UserProductListView.as_view(), name="product-list"),
    path('products/<slug>/', ProductDetailView.as_view(), name="product-detail"),
    path('products/<slug>/update/', ProductUpdateView.as_view(), name="product-update"),


    path('marketplace/', include('marketplace.urls', namespace="marketplace"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)