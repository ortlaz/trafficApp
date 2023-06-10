from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.admin import User

from traffic.app.models import Location, Status, Camera, Report


class UserSerializer(serializers.ModelSerializer):
    contract_number = serializers.SerializerMethodField(read_only=True)

    def get_contract_number(self, obj):
        return f"Д000{obj.id}"

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'contract_number']


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * email
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    video_path = serializers.CharField(source='videofile.file', read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Report
        fields = ("video_path", "date", "status")


class LocationsListSerializers(serializers.ModelSerializer):
    """Сериализатор списка локаций"""
    user = UserSerializer(read_only=True)
    contract_number = serializers.SerializerMethodField(read_only=True)
    status = StatusSerializer(read_only=True)

    def get_contract_number(self, obj):
        return f"Д000{obj.user.id}"

    class Meta:
        model = Location
        fields = ("id", "user", "contract_number", "address", "status")


class CameraSelectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ("id", "name",)


class LocationsSerializers(LocationsListSerializers):
    """Сериализатор локации"""
    user = UserSerializer(read_only=True)
    user_id = serializers.CharField(source='user.id')
    status = StatusSerializer(read_only=True)
    location_report = ReportSerializer(many=True, read_only=True)
    location_camera = CameraSelectListSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = (
            "user_id",
            "user",
            "contract_number",
            "address",
            "status",
            "location_report",
            "location_camera"
        )


class ContractSerializer(serializers.ModelSerializer):
    contract_number = serializers.SerializerMethodField(read_only=True)

    def get_contract_number(self, obj):
        return f"Д000{obj.id}"

    class Meta:
        model = User
        fields = ("id", "first_name", "contract_number")
