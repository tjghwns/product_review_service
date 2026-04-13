from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("products/", include("apps.products.urls")),
    path("reviews/", include("apps.reviews.urls")),
    path("interactions/", include("apps.interactions.urls")),
    path("ai/", include("apps.ai_gateway.urls")),
    path("", RedirectView.as_view(url="/products/", permanent=False)),  # ← 추가
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)