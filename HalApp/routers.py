from rest_framework.routers import DefaultRouter

from contacts.views import ContactViewSet, PhoneViewSet

router = DefaultRouter()

router.register(r'contacts', ContactViewSet)
router.register(r'phones', PhoneViewSet)