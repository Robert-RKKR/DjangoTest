# Django Import:
from django.forms.models import model_to_dict
from django.shortcuts import render
import threading

# Application Import:
from change_log.models import ChangeLog

def test(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    before_change = ChangeLog.objects.filter(
        object_name='TestModel',
        item_id=1,
    ).order_by('-changed')[1]
    after_change = ChangeLog.objects.filter(
        object_name='TestModel',
        item_id=1,
    ).latest('changed')

    # data['output'] = before_change
    data['before_change'] = before_change
    data['after_change'] = after_change
    
    # GET method:
    return render(request, 'test.html', data)

def test2(request):

    # Collect data to display:
    data = {
        'page_title': 'Test RKKR',
        'output': 'Welcome!',
    }

    output = ChangeLog.objects.get(pk=1)

    data['output'] = model_to_dict(output)
    
    # GET method:
    return render(request, 'test.html', data)
