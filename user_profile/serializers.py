from rest_framework import serializers
from user_profile.models import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=False)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'bio', 'location', 'birth_date', 'is_superuser', 'password', 'password2']
        extra_kwargs = {
            'is_superuser': {
                'read_only': True
            },
            'password': {
                'write_only': True,
                'required': False,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def update(self, user, validated_data):
        print(validated_data)
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.bio = validated_data.get('bio', user.bio)
        user.location = validated_data.get('location', user.location)
        user.birth_date = validated_data.get('birth_date', user.birth_date)
        if 'password' in validated_data or 'password2' in validated_data:
            password = validated_data.get('password', '')
            password2 = validated_data.get('password2', '')
            if password != password2:
                raise serializers.ValidationError({'password': 'Passwords must match.'})
            user.set_password(password)
        user.save()

        return user


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        return self.save()

    def save(self):
        user = User(
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user