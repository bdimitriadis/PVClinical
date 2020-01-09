from django.urls import path, re_path
from app import views


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    path('', views.index, name='index'),
    path('add-scenario', views.add_edit_scenario, name='add_scenario'),
    path('edit-scenario/<int:scenario_id>', views.add_edit_scenario, name='edit_scenario'),
    path('ajax/synonyms', views.get_synonyms, name='drugs_synonyms'),
    path('OpenFDAWorkspace_detailedView/', views.OpenFDAWorkspace_detailedView, name='OpenFDAWorkspace_detailedView'),
    path('OpenFDAWorkspace_detailedView/<int:scenario_id>', views.OpenFDAWorkspace_detailedView, name='OpenFDAWorkspace_detailedView'),
    # Permission denied
    path('denied', views.unauthorized, name='unauthorized'),
]
