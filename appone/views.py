from appone.tasks import process
from appone.models import Tasks
from appone.forms import itemForm
from django.shortcuts import render
from celery.result import AsyncResult
from django.views.decorators.http import require_http_methods, require_GET

@require_http_methods(["GET", "POST"])
def run(request):
    if request.method == "POST":
        form = itemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            item_name = data['item_name']
            item_status = data['item_status']
            process.delay(item_name=item_name, item_status=item_status)
            return render(request, 'item.html',
                          context={'form': itemForm,
                                   'message': f'{item_status} started...'})
    else:
        return render(request, 'item.html', context={'form': itemForm})


def track_item():
    entries = Tasks.objects.all()
    information = []
    for i in entries:
        progress = 100
        result = AsyncResult(i.task_id)
        if isinstance(result.info, dict):
            progress = result.info['progress']
        information.append([i.item_name, result.state, progress, i.task_id])
    return information

@require_GET
def controller(request):
    info = track_item()
    return render(request, 'controller.html', context={'info': info})

@require_GET
def cancel_item(request, task_id=None):
    result = AsyncResult(task_id)
    result.revoke(terminate=True)
    info = track_item()
    return render(request, 'controller.html', context={'info': info})


@require_GET
def delete_item(request, task_id=None):
    a = Tasks.objects.filter(task_id=task_id)
    a.delete()
    info = track_item()
    return render(request, 'controller.html', context={'info': info})
