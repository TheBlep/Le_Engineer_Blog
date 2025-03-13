from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Customizes the admin panel view for the :model:`about.About` model.
    --what this admin class does:
    --list the fields enhanced with Summernote
    Enhances the admin interface for the About model, enabling rich text
        editing for the `content` field using Summernote.
    **Summernote Fields:**
    ``content``
        The main content or description about the author, enhanced with
        Summernote WYSIWYG editor.
    """
    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel view for the :model:`about.CollaborateRequest`
    model.
    --what this admin class does:
    --list the fields displayed in the admin list view
    Displays collaboration requests in the admin panel, showing the message
    and read status.
    **List Display Fields:**
    ``message``
        The user's message or collaboration request details.
    ``read``
        A boolean flag indicating whether the request has been read.
    """
    list_display = ('message', 'read',)
