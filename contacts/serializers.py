from rest_framework import serializers

from contacts.models import Contact, Phone


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    telefono = PhoneSerializer()

    def create(self, validated_data):
        telefono = validated_data.pop('telefono', None)
        if telefono:
            phone = Phone.objects.get_or_create(**telefono)[0]
            validated_data['telefono'] = phone
        return Contact.objects.create(**validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['telefono'] = PhoneSerializer(instance.telefono).data
        return ret

    class Meta:
        model = Contact
        fields = '__all__'




