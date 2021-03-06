from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

User = get_user_model()

class UserDetailView(DetailView):
	template_name = 'accounts/user_detail.html'
	queryset = User.objects.all()

	def get_object(self):
		return get_object_or_404(User, username__iexact=self.kwargs.get("username") )

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(UserDetailView, self).get_context_data(*args, **kwargs)
	# 	following = UserProfile.objects.is_following(self.request.user, self.get_object())
	# 	context['following'] = following
	# 	context['recommended'] = UserProfile.objects.recommended(self.request.user)
	# 	return context