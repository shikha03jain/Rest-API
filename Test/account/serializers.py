from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404


class UserSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None,use_url=True)

    class Meta:
        model = User
        fields = ('id', 'firstname', 'lastname', 'email','image')

class MemberSerializer(serializers.ModelSerializer): #registering new members
    password = serializers.CharField(write_only='True')

    def create(self,validate_data):
        member = get_user_model().objects.create(
            username=validate_data['username'],
            email=validate_data['email']
        )

        member.set_password(validate_data['password'])
        member.save()
        return member
        """
        instance=member.save()
        instance.user=request.user
        instance.save()
        subject = 'Welcome'
        message = 'Hope to work with you soon'
        from_email = settings.EMAIL_HOST_USER
        to_list = [instance.email]

        send_mail(subject, message, from_email, to_list, fail_silently=True)
        #send_mail('Acknowledgement', 'Welcome to this Application', settings.EMAIL_HOST_USER, [instance.email], fail_silently=False)

        """

    class Meta:
        model = get_user_model()
        fields = ('username','email', 'password')
