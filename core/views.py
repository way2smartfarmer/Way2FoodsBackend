# views.py

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(["POST"])
def forgot_password(request):
    email = request.data.get("email")
    if email:
        user = User.objects.filter(email=email).first()
        if user:
            # Generate a token for the user
            token_generator = default_token_generator
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            # Build the password reset link
            # reset_password_link = f"http://{request.get_host()}/reset-password/?uid={uid}&token={token}"
            reset_password_link = f"http://localhost:300/reset-password/?uid={uid}&token={token}"

            # Send the password reset link to the user's email address
            send_mail(
                subject="Password reset",
                message=reset_password_link,
                from_email="way2agritechabi@gmail.com",
                recipient_list=[email],
                fail_silently=False,
            )

        return Response(
            {"message": "An email has been sent with instructions to reset your password."},
            status=status.HTTP_200_OK,
        )

    return Response(
        {"message": "Please provide an email address."},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["POST"])
def reset_password(request):
    uidb64 = request.data.get("uid")
    token = request.data.get("token")
    password1 = request.data.get("new_password")
    password2 = request.data.get("re_new_password")

    # Decode the uid to get the user id
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Check that the user and the token are valid
    token_generator = default_token_generator
    if user is not None and token_generator.check_token(user, token):
        if password1 == password2:
            user.set_password(password1)
            user.save()
            return Response(
                {"message": "Your password has been reset successfully."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Passwords do not match."},
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        return Response(
            {"message": "Invalid reset password link."},
            status=status.HTTP_400_BAD_REQUEST,
        )
