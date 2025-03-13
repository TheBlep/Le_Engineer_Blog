from django.urls import path

# Import views from the current application directory (where this file is located).
from . import views

# Define the URL patterns for the application.
urlpatterns = [
    # Route the root URL ('') to the `PostList` view, which is a class-based view.
    # The `as_view()` method is used to convert the class-based view into a callable view.
    # The name 'home' is assigned to this URL pattern for easy reference in templates or code.
    path('', views.PostList.as_view(), name='home'),

    # Route a URL with a slug (e.g., 'my-first-post') to the `post_detail` view function.
    # The `<slug:slug>` part captures the slug from the URL and passes it as an argument to the view.
    # The name 'post_detail' is assigned to this URL pattern.
    path('<slug:slug>/', views.post_detail, name="post_detail"),

    # Route a URL for editing a specific comment on a post.
    # The URL includes both the post's slug and the comment's ID.
    # The `<slug:slug>` captures the post's slug, and `<int:comment_id>` captures the comment's ID.
    # These are passed as arguments to the `comment_edit` view function.
    # The name 'comment_edit' is assigned to this URL pattern.
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),

    # Route a URL for deleting a specific comment on a post.
    # Similar to the previous pattern, it captures the post's slug and the comment's ID.
    # These are passed as arguments to the `comment_delete` view function.
    # The name 'comment_delete' is assigned to this URL pattern.
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]