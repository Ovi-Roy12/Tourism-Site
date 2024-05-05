from django.shortcuts import render, HttpResponseRedirect
from .models import Contact
from django.urls import reverse
from django.contrib import messages

def home(request):
    success_message = messages.get_messages(request)
    messages_to_display = [message.message for message in success_message]
    return render(request, 'App_Content/home.html', {'success_messages': messages_to_display})

def contact(request):
    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()

        messages.success(request, 'Thanks for contacting us!')
        return HttpResponseRedirect(reverse('App_Content:home'))
    return render(request,'App_Content/contact.html')


def My_Booking(request):
    return render(request,'App_Content/my_booking.html')

def view_details(request,destination_id):
     destinations = [
        {
            "id": 1,
            "name": "Cox's Bazar",
            "country": "Bangladesh",
            "description": "Beautiful beach destination...",
            "package": "4 days 5 nights",
            "price": "10,000 taka",
            "images": ["d1.jpg", "d2.jpg", "d3.jpg",],
        },
        {
            "id": 2,
            "name": "Tea Garden, Sylhet",
            "country": "Bangladesh",
            "description": "Scenic tea garden in Sylhet...",
            "package": "2 days 1 night",
            "price": "$5000",
            "images": ["d1.jpg", "d2.jpg", "d3.jpg"],
        },
        {
            "id": 3,
            "name": "Sundarban",
            "country": "Bangladesh",
            "description": "Explore the Sundarbans mangrove forest...",
            "package": "3 Days 2 nights",
            "price": "$700",
            "images": ["d1.jpg", "d2.jpg", "d3.jpg"],
        },
        {
            "id": 4,
            "name": "Sajek Valley, Bandarban",
            "country": "Bangladesh",
            "description": "Experience the beauty of Sajek Valley...",
            "package": "5 days 4 nights",
            "price": "$900",
            "images": ["d1.jpg", "d2.jpg", "d3.jpg"],
        },
    ]
     destination = next((d for d in destinations if d["id"] == destination_id), None)
     processed_images = [{"index": index, "image": image, "active": index == 0} for index, image in enumerate(destination["images"])]
     return render(request, 'App_Content/view_details.html', {'destination': destination,'processed_images': processed_images})


def search_results(request):
    search_query = request.GET.get('search', '')

    destinations = [
        {
            "id": 1,
            "name": "Cox's Bazar",
            "package": "4 days 5 nights",
            "images": ["d1.jpg"],
        },
        {
            "id": 2,
            "name": "Tea Garden, Sylhet",
            "package": "2 days 1 night",
            "images": ["d2.jpg"],
        },
        {
            "id": 3,
            "name": "Sundarban",
            "package": "3 Days 2 nights",
            "images": ["d3.jpg"],
        },
        {
            "id": 4,
            "name": "Sajek Valley, Bandarban",
            "package": "5 days 4 nights",
            "images": ["d4.jpg"],
        },
    ]

    filtered_destinations = [destination for destination in destinations if search_query.lower() in destination['name'].lower()]
    return render(request, 'App_Content/search_results.html', {'destinations': filtered_destinations, 'search_query': search_query, })
