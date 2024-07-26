from django.shortcuts import render, get_object_or_404
from .models import Word, Score, WordSet
import random

# Create your views here.
def match_voice(request, id):
    wordset = get_object_or_404(WordSet, id=id)
    words = wordset.words.order_by('?')[:12]
    words2 = list(words)
    random.shuffle(words2)

    return render(request, 'matchvoice.html', {'words1': words, 'words2': words2})


def gameover(request, id):
    wordset = get_object_or_404(WordSet, id=id)
    best_user_score = wordset.scores.filter(user=request.user).order_by('seconds').first()
    top_5_scores = wordset.scores.order_by('seconds')[:5]
    
    if request.method == 'POST':
        new_score = request.POST.get('new_score')
        if new_score:
            score_record = Score.objects.create(user=request.user, seconds=new_score, wordset=wordset)
            score_record.save()
    
    context = {
        'best_user_score': best_user_score,
        'top_5_scores': top_5_scores,
    }
    return render(request, 'gameover.html', context)