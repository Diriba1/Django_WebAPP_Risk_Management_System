from django.urls import path
from start1 import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('majorActivity/', views.majorActivity, name='majorActivity'),
    path('integralActivity/', views.integralActivity, name='integralActivity'),
    path('objective/', views.objective, name='objective'),
    path('inherentRisk/', views.inherentRisk, name='inherentRisk'),
    path('rmcdUser/', views.rmcdUser, name='rmcdUser'),
    path('iadUser/', views.iadUser, name='iadUser'),
    path('viewDetail/', views.viewDetail, name='viewDetail'),
    

    path('updateMajorActivity/<str:pk>/', views.updateMajorActivity, name='updateMajorActivity'),
    path('deleteMajorActivity/<str:pk>/', views.deleteMajorActivity, name='deleteMajorActivity'),

    path('createIntegralActivity/<str:pk>/', views.createIntegralActivity, name='createIntegralActivity'),
    path('updateIntegralActivity/<str:pk>/', views.updateIntegralActivity, name='updateIntegralActivity'),
    path('deleteIntegralActivity/<str:pk>/', views.deleteIntegralActivity, name='deleteIntegralActivity'),

    path('createObjective/<str:pk>/', views.createObjective, name='createObjective'),
    path('updateObjective/<str:pk>/', views.updateObjective, name='updateObjective'),
    path('deleteObjective/<str:pk>/', views.deleteObjective, name='deleteObjective'),
    
    path('createRisk/<str:pk>/', views.createRisk, name='createRisk'),
    path('updateInherentRisk/<str:pk>/', views.updateInherentRisk, name='updateInherentRisk'),
    path('deleteInherentRisk/<str:pk>/', views.deleteInherentRisk, name='deleteInherentRisk'),

    path('updateRmcdUser/<str:pk>/', views.updateRmcdUser, name='updateRmcdUser'),
    path('updateIadUser/<str:pk>/', views.updateIadUser, name='updateIadUser'),
    
]