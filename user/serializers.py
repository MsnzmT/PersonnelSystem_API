from rest_framework import serializers
from .models import Person
from trip.models import TripAdmin
from salary.models import PaySalaryAdmin
from news.models import NewsAdmin



class TripAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripAdmin
        fields = ('is_trip_admin',)

class PaySalaryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaySalaryAdmin
        fields = ('is_paysalary_admin',)

class NewsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAdmin
        fields = ('is_news_admin',)

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ('id', 'personnelNumber', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'role', 'profile_picture')

    def get_role(self, obj):
        if hasattr(obj, 'tripadmin') and obj.tripadmin.is_trip_admin:
            return 'tripadmin'
        elif hasattr(obj, 'paysalaryadmin') and obj.paysalaryadmin.is_paysalary_admin:
            return 'paysalaryadmin'
        elif hasattr(obj, 'newsadmin') and obj.newsadmin.is_news_admin:
            return 'newsadmin'
        elif hasattr(obj, 'leaveadmin') and obj.leaveadmin.is_leave_admin:
            return 'leaveadmin'
        else:
            return 'employee'