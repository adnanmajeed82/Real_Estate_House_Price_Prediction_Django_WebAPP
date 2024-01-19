# prediction/views.py
from django.shortcuts import render, redirect
from .forms import HouseForm
from .models import PredictionResult
from .predictor import predict_price  # Create a separate file for machine learning predictions

def predict(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house_instance = form.save()
            predicted_price = predict_price(house_instance.area, house_instance.bedrooms, house_instance.bathrooms)
            PredictionResult.objects.create(house=house_instance, predicted_price=predicted_price)
            return redirect('result')
    else:
        form = HouseForm()

    return render(request, 'prediction/predict.html', {'form': form})

def result(request):
    results = PredictionResult.objects.all()
    return render(request, 'prediction/result.html', {'results': results})
