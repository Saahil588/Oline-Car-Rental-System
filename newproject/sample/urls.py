from django.urls import path
# from .import views as v
from .views import *

urlpatterns = [
    path('',home,name='homepage'),
    path('about/',about,name='aboutpage'),
    path('service/',service,name='service'),
    path('terms/',terms,name='terms'),
    path('register/',register,name='register'),
    path('adminbase/',adminbase,name='adminbase'),
    path('userbase/',userbase,name='userbase'),
    path('admin_fn/',admin_fn,name='admin_fn'),
    path('user_fn/',user_fn,name='user_fn'),
    path('editprofile/',edit_profile,name='editprofile'),
    path('changeps/',change_password,name='changeps'),


    path('contact/',contact,name='contact'),
    path('viewcontact/',view_contact,name='viewcontact'),
    path('deletecontact/<int:id>/',del_contact,name='delcontact'),

    path('car/',car,name='car'),
    path('admincar/',admincar,name='admincar'),
    path('view_car/',adview_car,name='viewcar'),
    path('editcar/<int:id>/',edit_admincar,name='edit_car'),
    path('deletecar/<int:id>/',del_admincar,name='delete_car'),

    path('addcar/',addcar,name='addcar'),
    path('useraddcar/',user_addcar,name='useraddcar'),
    path('view_addcar/',adview_addcar,name='viewaddcar'),
    path('editaddcar/<int:id>/',edit_adminaddcar,name='edit_addcar'),
    path('deleteaddcar/<int:id>/',del_adminaddcar,name='delete_addcar'),

    path('adminoffer/',adminoffer,name='adminoffer'),
    path('offers/',offers,name='offers'),
    path('viewoffer/',adview_offer,name='viewoffer'),
    path('editoffer/<int:id>/',edit_adminoffer,name='edit_offer'),
    path('deleteoffer/<int:id>/',del_adminoffer,name='delete_offer'),
    path('offer_images/<int:id>/',offer_images,name='offer_images'),

    path('image_upload/',adminimage,name='image_upload'),
    path('user_image/',user_image,name='user_image'),
    path('editimage/<int:id>/',edit_adminimage,name='edit_image'),
    path('deleteimage/<int:id>/',del_adminimage,name='delete_image'),
    path('viewimage/',adview_image,name='viewimage'),

    path('booking/<int:id>/',booking,name='booking'),
    path('viewbooking/',view_booking,name='viewbooking'),
    path('deletebooking/<int:id>/',delete_booking,name='delete_booking'),

    path('car_booking/<int:id>/',car_booking,name='car_booking'),
    path('viewcarbooking/',view_carbooking,name='viewcarbooking'),
    path('deletecarbooking/<int:id>/',delete_carbooking,name='delete_carbooking'),

    path('offer_booking/<int:id>/',offer_booking,name='offer_booking'),
    path('viewofferbooking/',view_offerbooking,name='viewofferbooking'),
    path('deleteofferbooking/<int:id>/',delete_offerbooking,name='delete_offerbooking'),

    path('viewuser/',view_user,name='viewuser'),
    path('deleteuser/<int:id>/',delete_user,name='delete_user'),

    path('userview/',user_view,name='user_view'),
    path('deleteuserview/<int:id>/',delete_userview,name='delete_userview'),

    path('userviewbook/',user_viewcarbook,name='user_viewcarbook'),
    path('deletecarbook/<int:id>/',delete_carbook,name='delete_carbook'),

    path('userviewoffer/',user_viewoffer,name='user_viewoffer'),
    path('deleteuseroffer/<int:id>/',delete_useroffer,name='delete_useroffer'),



    path('logout/',logout_admin,name='logout'),
    path('login/',login_user,name='login'),
    path('logoutuser/',login_user,name='logout_user'),
    path('logout_admin/',logout_admin,name='logout_admin'),
    

]