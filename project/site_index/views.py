import requests
from django.shortcuts import render


def get_site_index(zip_code):
    url = f'https://api.zippopotam.us/RU/{ zip_code }'
    response = requests.get(url)
    data = response.json()
    return data


def site_index_view(request):
    if request.method == 'POST':
        zip_code = request.POST.get('zip_code')
        data = get_site_index(zip_code)

        context = {
            'city': data['places'][0]['place name'],
            'latitude': data['places'][0]['latitude'],
            'longitude': data['places'][0]['longitude'],
            'district': data['places'][0].get('district', 'Нет данных'),
            'short_district': data['places'][0].get('short_district', 'Нет данных'),
        }
        return render(request, 'zip_code.html', context)

    return render(request, 'zip_code.html')
