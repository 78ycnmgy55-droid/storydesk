from django.shortcuts import render, redirect, get_object_or_404
from .models import Story, Topic
from .forms import StoryForm, TopicForm


def story_list(request):
    stories = Story.objects.all()

    status = request.GET.get('status')
    if status:
        stories = stories.filter(status=status)

    sort = request.GET.get('sort', 'newest')

    if sort == 'title':
        stories = stories.order_by('title')
    else:
        stories = stories.order_by('-created_at')

    context = {
        'stories': stories,
        'selected_status': status,
        'selected_sort': sort,
    }

    return render(request, 'stories/story_list.html', context)

def story_create(request):
    from django.shortcuts import render, redirect, get_object_or_404
    def story_detail(request, pk):
        story = get_object_or_404(Story, pk=pk)
        return render(request, 'stories/story_detail.html', {'story': story})
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('story_list')
    else:
        form = StoryForm()

    return render(request, 'stories/story_form.html', {'form': form})


# def topic_create(request):
#     if request.method == 'POST':
#         form = TopicForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('story_list')
#     else:
#         form = TopicForm()

    return render(request, 'stories/topic_form.html', {'form': form})
def topic_create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():
            form.save()
            return render(
                request,
                'stories/topic_form.html',
                {
                    'form': TopicForm(),
                    'success': 'Темата е записана успешно!'
                }
            )
    else:
        form = TopicForm()

    return render(
        request,
        'stories/topic_form.html',
        {'form': form}
    )
def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'stories/story_detail.html', {'story': story})
def story_edit(request, pk):
    story = get_object_or_404(Story, pk=pk)

    if request.method == 'POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm(instance=story)

    return render(request, 'stories/story_form.html', {'form': form})
def story_delete(request, pk):
    story = get_object_or_404(Story, pk=pk)

    if request.method == 'POST':
        story.delete()
        return redirect('story_list')

    return render(
        request,
        'stories/story_confirm_delete.html',
        {'story': story}
    )