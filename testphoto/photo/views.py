from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.views import generic

from taggit.models import Tag, TaggedItem

from .models import Photo


class PhotoListView(generic.ListView):
    """
    Renders list of photo
    """
    context_object_name = "photo_list"
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        """
        View for displaying a list of objects.
        """
        slug = kwargs.get('slug')

        qs = Photo.objects.filter(
            pk__in=TaggedItem.objects.filter(
                tag__in=Tag.objects.filter(slug__in=slug.split(',')),
                content_type=ContentType.objects.get_for_model(Photo.objects.model)
            ).values_list("object_id", flat=True)
        )
        if 'sort' in kwargs.keys():
            qs = qs.order_by(kwargs.get('sort'))
        else:
            qs = qs.order_by('-created')

        self.object_list = qs
        kwargs.update(object_list=self.object_list)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)