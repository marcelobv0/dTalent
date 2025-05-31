from django.urls import path
from .views import CustomAuthToken, UserListView, UserDetailView

#endpoints desde el endpoint /users/
urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='user-login'),
    path('', UserListView.as_view(), name='user-list'),             #  nos habilita el endpoint GET /users/
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail') #  nos habilita endpoints como GET /users/1
]