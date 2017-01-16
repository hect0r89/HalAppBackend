from rest_framework.routers import DefaultRouter

from contacts.views import ContactViewSet, EmailViewSet, PhoneViewSet

router = DefaultRouter()

router.register(r'contacts', ContactViewSet)
router.register(r'emails', EmailViewSet)
router.register(r'phones', PhoneViewSet)