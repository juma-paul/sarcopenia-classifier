from django.shortcuts import render, redirect, get_object_or_404
from .forms import DataForm, ModelTwoForm, ModelThreeForm
from .models import Data, ModelTwo, ModelThree

def index(request):
    form = DataForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.save()
        return redirect('diagnosis', data_id=data.pk)
    return render(request, 'sarcopenia/index.html', {'form': form})

def diagnosis(request, data_id):
    data = get_object_or_404(Data, pk=data_id)
    if data.additional_data_required:
        if data.additional_model_used == 'model2':
            return redirect('model_two', data_id=data_id)
        elif data.additional_model_used == 'model3':
            if hasattr(data, 'model_two_data'):
                return redirect('model_three', model_two_id=data.model_two_data.id)
    return render(request, 'sarcopenia/results.html', {'data': data})

def model_two(request, data_id):
    data = get_object_or_404(Data, pk=data_id)
    form = ModelTwoForm(request.POST or None, instance=data.model_two_data if hasattr(data, 'model_two_data') else None)
    if request.method == 'POST':
        if form.is_valid():
            model_two = form.save(commit=False)
            model_two.data = data
            model_two.save()
            return redirect('diagnosis', data_id=data_id)
    return render(request, 'sarcopenia/model_two.html', {'form': form, 'data': data})

def model_three(request, model_two_id):
    model_two = get_object_or_404(ModelTwo, pk=model_two_id)
    form = ModelThreeForm(request.POST or None, instance=model_two.model_three_data if hasattr(model_two, 'model_three_data') else None)
    if request.method == 'POST':
        if form.is_valid():
            model_three = form.save(commit=False)
            model_three.model_two = model_two
            model_three.save()
            return redirect('diagnosis', data_id=model_two.data.pk)
    return render(request, 'sarcopenia/model_three.html', {'form': form, 'model_two': model_two})
