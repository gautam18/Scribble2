from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .models import Entry,Profile,Likes,Saves,Follow,Writing_Style,Genre
from .forms import UserForm,LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User,Group
from django.http import HttpResponseRedirect








class IndexView(LoginRequiredMixin,generic.ListView):
	template_name='Entry/index.html'
	context_object_name='entry_list'
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	redirect_unauthenticated_users =True
	#raise_exception = True


	def get_queryset(self):
		return Entry.objects.all()

class FollowIndexView(LoginRequiredMixin,generic.ListView):
	template_name='Entry/follow.html'
	context_object_name='follow_list'
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	redirect_unauthenticated_users =True

	def get_queryset(self):

		return Follow.objects.filter(follower=self.kwargs['user_id'])

class FollowedByIndexView(LoginRequiredMixin,generic.ListView):
	template_name='Entry/followedby.html'
	context_object_name='followedby_list'
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	redirect_unauthenticated_users =True

	def get_queryset(self):

		return Follow.objects.filter(following=self.kwargs['user_id'])

class MyWorks(LoginRequiredMixin,generic.ListView):
	template_name='Entry/myworks.html'
	context_object_name='entry_list'
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	redirect_unauthenticated_users =True
	#raise_exception = True


	def get_queryset(self):
		return Entry.objects.all()

class MyLikes(LoginRequiredMixin,generic.ListView):
	template_name='Entry/mylikes.html'
	context_object_name='entry_list'
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	redirect_unauthenticated_users =True
	#raise_exception = True


	def get_queryset(self):
		return Entry.objects.all()

class MyBookmarks(LoginRequiredMixin,generic.ListView):
	template_name='Entry/mybookmarks.html'
	context_object_name='entry_list'
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	redirect_unauthenticated_users =True
	#raise_exception = True


	def get_queryset(self):
		return Entry.objects.all()



class DetailView(LoginRequiredMixin, generic.DetailView):
	model=Entry
	template_name='Entry/detail.html'
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	#raise_exception = True
	redirect_unauthenticated_users= True


class UserDetailView(LoginRequiredMixin, generic.DetailView):
	model=User
	template_name='Entry/userdetail.html'
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	#raise_exception = True
	redirect_unauthenticated_users= True


class EntryCreate(LoginRequiredMixin, CreateView):
	model=Entry
	fields=['entry_name','entry_description','entry_style','entry_genres','entry_writer_id']
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	#raise_exception = True
	redirect_unauthenticated_users= True


class EntryUpdate(LoginRequiredMixin, UpdateView):
	model=Entry
	fields=['entry_name','entry_description','entry_style','entry_writer_id','entry_release_date']
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	#raise_exception = True
	redirect_unauthenticated_users= True

class ProfileCreate(LoginRequiredMixin, CreateView):
	model=Profile
	fields=['user','birth_date']
	login_url="/entry/login"
	redirect_field_name = "rollback"
	#raise_exception = True
	redirect_unauthenticated_users= True

class ProfileUpdate(LoginRequiredMixin, UpdateView):
	model=Profile
	print 'hello'
	fields=['user','birth_date']
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	#raise_exception = True
	redirect_unauthenticated_users= True

class ProfileDelete(LoginRequiredMixin,DeleteView):
	model=Profile
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	#raise_exception = True
	redirect_unauthenticated_users= True

	def get_success_url(self):

		return reverse_lazy('Entry:index')


class EntryDelete(LoginRequiredMixin,DeleteView):
	model=Entry
	login_url = "/entry/login/"
	redirect_field_name = "rollback"
	#raise_exception = True
	redirect_unauthenticated_users= True

	def get_success_url(self):

		return reverse_lazy('Entry:index')
	





class LoginFormView(View):
	form_class=LoginForm
	template_name='Lab/login.html'

	#display blank form	
	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})
	

	# process form data
	def post(self,request):
		form=self.form_class(request.POST)

			
		if form.is_valid():
		#cleaned data (formatted)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			
			print username ,password

			#returns User object if credentials are correct

			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					  
					return redirect('/entry')
				else:
					return HttpResponse("You're account is disabled.")
			else:
				  # Return an 'invalid login' error message.
				print  "invalid login details username password"
				return render(request,self.template_name,{'form':form})

	

class UserFormView(View):
	template_name='Lab/registration.html'



	#display blank form	
	def get(self,request):
		form=UserForm(None)
		return render(request,self.template_name,{
			'form':form,
			})
	

	# process form data
	def post(self,request):
		form=UserForm(request.POST)

		if form.is_valid() :

			user=form.save(commit=False)

			#cleaned data (formatted)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']


			user.set_password(password)
			
			user.save()
			user.groups.add(Group.objects.get(name='User'))
			
			return redirect('/entry/login')
		return render(request,self.template_name,{
			'form':form
			})


class ReviewerFormView(View):
	template_name='Entry/registration_index.html'



	#display blank form 
	def get(self,request):
		form=UserForm(None)
		return render(request,self.template_name,{
			'form':form,
			})
	

	# process form data
	def post(self,request):
		form=UserForm(request.POST)

		if form.is_valid() :

			user=form.save(commit=False)

			#cleaned data (formatted)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']


			user.set_password(password)
			user.save()
			user.groups.add(Group.objects.get(name='Reviewer'))
			return redirect('/entry/login')
		return render(request,self.template_name,{
			'form':form
			})

def like(request,entry_id):
	entry=get_object_or_404(Entry,pk=entry_id)
	likes=Likes(user=request.user,entry=entry)
	likes.save()
	return redirect('/entry/')


def rate(request,entry_id):

	entry=get_object_or_404(Entry,pk=entry_id)


	

	return




def bookmark(request,entry_id):

	entry=get_object_or_404(Entry,pk=entry_id)
	bookmark=Saves(user=request.user,entry=entry)
	bookmark.save()
	return redirect('/entry/')


def follow(request,pk):
	following=get_object_or_404(User,pk=pk)
	follower=request.user
	follow=Follow(following=following,follower=follower)
	follow.save()
	return redirect('/entry/')


	return 

def search(request):
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET': # If the form is submitted

		search_query = request.GET.get('search_box', None)
		# Do whatever you need with the word the user looked for

		entry1=Entry.objects.filter(entry_name=search_query)

		
		style=Writing_Style.objects.filter(writing_style=search_query)
		
		entry2=Entry.objects.filter(entry_style=style)
		
		author=User.objects.filter(username=search_query)
		
		entry3=Entry.objects.filter(entry_writer_id=author)
		
		genre=Genre.objects.filter(genre_name=search_query)

		entry4=Entry.objects.filter(entry_genres =genre )

		

		entry_list=(entry1 | entry2 | entry3 | entry4).distinct()
		
		context={
		'entry_list':entry_list
		}

    return render(request,'Entry/searchresults.html',context)

