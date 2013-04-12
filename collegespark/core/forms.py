from django import forms


class LoginForm(forms.Form):
    email_login = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email',
               'class': 'input-small',
               'placeholder': 'Email'}))

    password_login = forms.CharField(widget=forms.PasswordInput(
        render_value=False, attrs={'class': 'input-small',
                                   'placeholder': 'Password'}))


class SignUpForm(forms.Form):
    email_signup = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email',
               'placeholder': 'Your Email'}))

    school_signup = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your School Name'}))

    password_signup = forms.CharField(widget=forms.PasswordInput(
        render_value=False, attrs={'class': 'password',
                                   'placeholder': 'Password'}))

    re_enter_password_signup = forms.CharField(widget=forms.PasswordInput(
        render_value=False, attrs={'placeholder': 'Re-enter Password'}))