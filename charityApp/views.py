from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from charityApp.models import *
from django.db.models import Q
from django.contrib import messages
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'Home/home.html')

class About(View):
    def get(self, request):
        about = AboutUS.objects.all()
        context = {
                'about':about
        }
        return render(request, 'Home/about.html', context)

class ContactUs(View):
	def get(self, request):
		return render(request, 'Home/contact.html')

	def post(self, request):
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		user_contact = request.POST['user_contact']
		message = request.POST['message']

		cont = Contact(

			first_name = first_name,
			last_name = last_name,
			email = email,
			user_contact = user_contact,
			message = message

			)
		cont.save()
		messages.success(request, 'You message has been sent!')
		return render(request, 'Home/contact.html')
		

class Registration(View):
	def get(self, request):
		return render(request, 'Home/registration.html')
	def post(self, request):
		mem_name = request.POST['mem_name']
		mem_email = request.POST['mem_email']
		mem_contact = request.POST['mem_contact']
		mem_address = request.POST['mem_address']
		mem_image = request.POST['mem_image']

		register =  Members(
			mem_name=mem_name,
			mem_email=mem_email,
			mem_contact=mem_contact,
			mem_address=mem_address,
			mem_image=mem_image

			)
		register.save()
		messages.success(request, 'You are registered successfully!')
		return render(request, 'Home/registration.html')

class ImgGallery(View):
	def get(self, request):
		images = ImageGallery.objects.all()
		videos = VideoGallery.objects.all()
		context = {

			'images':images,
			'videos':videos
		}
		return render(request, 'Home/gallery.html', context)

class SmcsEvents(View):
	def get(self, request):
		event = Events.objects.all()
		context = {

			'event': event
		}

		return render(request, 'Home/events.html', context)

class EventDetail(View):
	def get(self, request, id, slug):
		event = get_object_or_404(Events, id=id, slug=slug)

		context = {

			'event': event
		}

		return render(request, 'Home/event_detail.html', context)


