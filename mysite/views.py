from django.shortcuts import render
from django.contrib.auth import logout
from .forms import SignUpForm
from django.contrib.auth import authenticate
from django.views import View
from django.views.generic.edit import FormView




class SignUpView(FormView):

	signupform = SignUpForm

	def get(self, request, *args, **kwargs):

		signupform = self.signupform()
		context = {'signupform': signupform,}

		return render(request, 'registration/signup.html', context)


	def post(self, request, *arsg, **kwargs):

		signupform = self.signupform(request.POST)

		if signupform.is_valid():

			print('VALID')
			signupform.save()


		context = {'signupform': signupform,}

		return render(request, 'registration/signup.html', context)






def logout_view(request):
    logout(request)

    return render(request, 'registration/logged_out.html')
