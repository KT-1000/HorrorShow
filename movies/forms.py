from django.forms import ModelForm
from movies.models import Collection


class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = ['title', 'description', 'creation_date', 'movies']
