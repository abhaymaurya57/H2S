from django.shortcuts import render
from django.http import JsonResponse
from .models import ModeratedText

# Sample list of hateful words
def base(request):
    return render(request,"base.html")

def submit(request):
    return render(request,"submit.html")
HATEFUL_KEYWORDS = ["hate", "stupid", "idiot","i love you","utkarsh","pratyush","sumit","abuse", "abuser", "animal", "ape", "assault", "awful", "bad", "barbaric",
    "bigot", "bigotry", "biased", "bitch", "brutal", "bully", "cancer", "ch*nk",
    "clown", "cockroach", "criminal", "cunt", "damn", "deadbeat", "delusional",
    "demon", "disgusting", "disgrace", "dumb", "enemy", "evil", "extremist",
    "failure", "fake", "fraud", "garbage", "harass", "hate", "hatred", "hell",
    "horrible", "idiot", "ignorant", "illegal", "imbecile", "inferior", "insane",
    "insult", "jerk", "joke", "kill", "loser", "lunatic", "menace", "moron",
    "nasty", "nazi", "nonsense", "offensive", "oppressor", "parasite", "pathetic",
    "pervert", "pest", "pig", "psycho", "racist", "rapist", "reject", "repulsive",
    "rubbish", "scum", "shameful", "sick", "slavery", "slur", "stupid", "terrorist",
    "thief", "threat", "trash", "ugly", "unworthy", "useless", "villain", "violent",
    "vulgar", "weak", "worthless", "wretched",'chod','madharchod','bahanchod','fuckyou','bkl','bahan ki lawri',"bsdk",
]

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def analyze_text(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        is_hateful = any(word in text.lower() for word in HATEFUL_KEYWORDS)

        # Save to database (optional)
        ModeratedText.objects.create(text=text, is_hateful=is_hateful)

        return render(request, "submit.html", {"result": "hateful" if is_hateful else "safe"})
    
    return render(request, "submit.html", {"error": "Invalid request"}, status=400)
