from django.db import models
from cloudinary.models import CloudinaryField

# Django models used:

class About(models.Model):
    """
    Represents information about the website author.
    --from which model this view displays data:
    --list the fields included in the model and their purpose
    Stores details about the author, including a title, profile image, update timestamp, and content.
    **Fields:**
    ``title``
        The title of the about section.
    ``profile_image``
        The profile image of the author, stored using Cloudinary.
    ``updated_on``
        The timestamp of the last update, automatically set to the current time on save.
    ``content``
        The main content or description about the author.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Represents a collaboration request submitted by a user.
    --from which model this view displays data:
    --list the fields included in the model and their purpose
    Stores details of collaboration requests, including the user's name, email, message, and read status.
    **Fields:**
    ``name``
        The name of the user submitting the request.
    ``email``
        The email address of the user for contact purposes.
    ``message``
        The user's message or collaboration request details.
    ``read``
        A boolean flag indicating whether the request has been read (defaults to False).
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"