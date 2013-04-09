from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email',
               'class': 'input-small',
               'placeholder': 'Email'}))

    password = forms.CharField(widget=forms.PasswordInput(
        render_value=False, attrs={'class': 'input-small',
                                   'placeholder': 'Password'}))


class SignUpForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email',
               'placeholder': 'Your Email'}))

    school = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Your School Name'}))

    password = forms.CharField(widget=forms.PasswordInput(
        render_value=False, attrs={'placeholder': 'Password'}))

    re_enter_password = forms.CharField(widget=forms.PasswordInput(
        render_value=False, attrs={'placeholder': 'Re-enter Password'}))