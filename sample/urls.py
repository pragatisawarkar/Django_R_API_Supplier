from sample.views import *
from rest_framework.routers import SimpleRouter


routing=SimpleRouter()

routing.register('customer',CustomerOp)
routing.register('address',AddressOp)

urlpatterns=routing.urls