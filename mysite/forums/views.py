from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from forums.models import Forum, Comment
from forums.forms import CommentForm

from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


# Create your views here.
class ForumListView(OwnerListView):
    model = Forum
    template_name = 'forums/list.html'


class ForumDetailView(OwnerListView):
    model = Forum
    template_name = 'forums/detail.html'

    def get(self, request, pk):
        x = Forum.objects.get(id=pk)
        comments = Comment.objects.filter(forum=x).order_by('-updated_at')
        comment_form = CommentForm()
        cntx = {'forum': x, 'comments': comments, 'comment_form': comment_form}
        return render(request, self.template_name, cntx)


class ForumCreateView(OwnerCreateView):
    model = Forum
    fields = ['title', 'text']
    template_name = 'forums/form.html'


class ForumUpdateView(OwnerUpdateView):
    model = Forum
    fields = ['title', 'text']
    template_name = 'forums/form.html'


class ForumDeleteView(OwnerDeleteView):
    model = Forum
    template_name = "forums/delete.html"


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        f = get_object_or_404(Forum, id=pk)
        comment = Comment(
            text=request.POST['comment'], owner=request.user, forum=f)
        comment.save()
        return redirect(reverse('forums:forum_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "forums/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        forum = self.object.forum
        return reverse('forums:forum_detail', args=[forum.id])
