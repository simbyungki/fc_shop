from django import forms
from .models import Fcuser

class RegisterForm(forms.Form) : 
	email = forms.EmailField(
		error_messages = {
			'required' : '이메일을 입력해주세요.'
		},
		max_length = 64, label = '이메일'
	)
	password = forms.CharField(
		error_messages = {
			'required' : '비밀번호를 입력해주세요.'
		},
		widget = forms.PasswordInput, label = '비밀번호'
	)
	re_password = forms.CharField(
		error_messages = {
			'required' : '비밀번호를 입력해주세요.'
		},
		widget = forms.PasswordInput, label = '비밀번호 확인'
	)

	def clean(self) : 
		cleaned_data = super().clean()
		email = cleaned_data.get('email')
		password = cleaned_data.get('password')
		re_password = cleaned_data.get('re_password')
	
		if password and re_password : 
			if password != re_password : 
				self.add_error('re_password', '비밀번호를 다시 확인해주세요.')
			else : 
				fcuser = Fcuser(
					email = email,
					password = password
				)
				fcuser.save()