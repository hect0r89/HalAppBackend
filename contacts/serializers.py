from rest_framework import serializers

from contacts.models import Contact, Email, Phone


class ContactSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['phones'] = PhoneSerializer(instance.phones, many=True).data
        ret['emails'] = EmailSerializer(instance.emails, many=True).data
        return ret

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'emails', 'phones')


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = ('id', 'address', 'type', 'contact')


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = ('id', 'number', 'type', 'contact')

