from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
   

    #endpoint for listing the vendors
   
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),

    
    path("vendors/",views.VendorListCreateView.as_view(),name="Vendor_list"),
    path('vendors/<int:pk>/',views.VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('purchase_orders/',views. PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
    path('vendors/<int:pk>/performance/',views. VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:pk>/acknowledge/',views. AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),

]
