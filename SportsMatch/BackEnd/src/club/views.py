from django.shortcuts import render
from .forms import ClubCreate
# Create your views here.


from .models import Club



def club_create_view(request):
	form = ClubCreate(request.POST or None)
	if form.is_valid():
		form.save()
		form = ClubCreate()

	context = {
		'form': form
	}


	return render(request, "/Users/ithamarezra/Documents/GitHub/Sports-Match/SportsMatch/FrontEnd/club_create.html", context)



def club_detail_view(request):
	obj = Club.objects.get(id=1)
	context = {
		"obj": obj,
	}


	return render(request, "/Users/ithamarezra/Documents/GitHub/Sports-Match/SportsMatch/FrontEnd/detail.html", context)