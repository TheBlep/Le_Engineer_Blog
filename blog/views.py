from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Class-based view to list posts
class PostList(generic.ListView):
    queryset = Post.objects.filter(author=1)  # Filter posts by author ID 1
    template_name = "blog/index.html"  # Template to render
    paginate_by = 6  # Number of posts per page

# View to display a single post and handle comments
def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)  # Filter published posts
    post = get_object_or_404(queryset, slug=slug)  # Get post or 404
    comments = post.comments.all().order_by("-created_on")  # Get comments, newest first
    comment_count = post.comments.filter(approved=True).count()  # Count approved comments

    if request.method == "POST":  # Handle comment submission
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user  # Set comment author
            comment.post = post  # Associate comment with post
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')

    comment_form = CommentForm()  # Empty form for new comments

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

# View to edit a comment
def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)  # Get post
        comment = get_object_or_404(Comment, pk=comment_id)  # Get comment
        comment_form = CommentForm(data=request.POST, instance=comment)  # Populate form with comment data

        if comment_form.is_valid() and comment.author == request.user:  # Validate form and user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Reset approval status
            comment.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))  # Redirect to post detail

# View to delete a comment
def comment_delete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)  # Get post
    comment = get_object_or_404(Comment, pk=comment_id)  # Get comment

    if comment.author == request.user:  # Ensure user owns the comment
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))  # Redirect to post detail