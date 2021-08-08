from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(request):
    context = {
        "articles": [
            {
                "title": "رئیس کل بانک مرکزی در پاسخ به باشگاه خبرنگاران جوان:",
                "description": "کمیجانی گفت به گلا دست نزنین.",
                "image": "https://cdn.yjc.news/files/fa/news/1400/5/17/14481305_958.jpg"
            },
            {
                "title": "رئیس شورای شهر تهران:",
                "description": "چمران گفت به گلا دست نزنین.",
                "image": "https://cdn.yjc.news/files/fa/news/1400/5/17/14480399_203.jpg"
            },
            {
                "title": "ازار خودرو زیر ذره بین باشگاه خبرنگاران جوان؛",
                "description": "قیمت خودرو، امروز در بازار آزاد نسبت به آخرین معاملات دیروز با افزایش ",
                "image": "https://cdn.yjc.news/files/fa/news/1400/5/17/14481136_464.jpg"
            }
        ]
    }
    return render(request, "blog/home.html", context)

