from django.urls import path
from .views import EntriesList, CreateEntry, EntriesDetail, DeleteEntry, UpdateEntry, SearchEntry

urlpatterns = [

    path('', EntriesList.as_view(), name='home'),
    path('search/', SearchEntry.as_view(), name='search-entry'),
    path('create/', CreateEntry.as_view(), name='create-entry'),
    path('delete/<int:pk>', DeleteEntry.as_view(), name='delete-entry'),
    path('update/<int:pk>', UpdateEntry.as_view(), name='update-entry'),
    path('detail/<int:pk>', EntriesDetail.as_view(), name='entry-detail'),
]