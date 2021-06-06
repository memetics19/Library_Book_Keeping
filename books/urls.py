from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserView,CreateTokenView,ManageUserView,BookBorrowViewSet,BookReturnViewset
router = DefaultRouter()
router.register('borrow', BookBorrowViewSet)
router.register('return',BookReturnViewset)

app_name = 'books'

urlpatterns = [
    path('',include(router.urls)),
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name="token"),
    path('me/', ManageUserView.as_view(), name="me"),
]