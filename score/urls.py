from django.urls import path
from . import views

urlpatterns = [
    # Evaluator authentication
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('logout/', views.logout_view, name='logout_view'),

    # Scoring
    path('submit/', views.submit_score, name='submit_score'),

    # Coordinator actions
    path('dashboard/', views.coordinator_dashboard, name='dashboard'),
    path('download/', views.download_results_csv, name='download_results'),
    path('import-students/', views.import_students_from_excel, name='import_students'),
]
