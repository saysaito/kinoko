from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Vote

def index(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        if choice in [Vote.KINOKO, Vote.TAKENOKO]:
            Vote.objects.create(choice=choice)
        return redirect('results')
    return render(request, 'vote/index.html')

def results(request):
    results = Vote.objects.values('choice').annotate(
        count=Count('choice')
    ).order_by('-count')
    
    total_votes = Vote.objects.count()
    results_dict = {item['choice']: {
        'count': item['count'],
        'percentage': round(item['count'] * 100 / total_votes, 1) if total_votes > 0 else 0
    } for item in results}
    
    context = {
        'kinoko_data': results_dict.get(Vote.KINOKO, {'count': 0, 'percentage': 0}),
        'takenoko_data': results_dict.get(Vote.TAKENOKO, {'count': 0, 'percentage': 0}),
        'total_votes': total_votes,
    }
    return render(request, 'vote/results.html', context)
