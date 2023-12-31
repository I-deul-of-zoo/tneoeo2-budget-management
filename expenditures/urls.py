from django.urls import path
from .views import SetExpendituresListView,SetExpendituresDetailView,ExpenditureNotiView, ExpenditureReciView
app_name = "expenditures"

urlpatterns = [
   path('',  SetExpendituresListView.as_view(), name='expenditures-crud'),
   path('<int:pk>/',  SetExpendituresDetailView.as_view(), name='expenditures-crud'),
   path('noti/',  ExpenditureNotiView.as_view(), name='expenditures-noti'),
   path('rec/',  ExpenditureReciView.as_view(), name='expenditures-rec'),
]