from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    """
    Serializer fields in a human readable format:
    """
    code = serializers.SerializerMethodField('get_status_code')
    response = serializers.SerializerMethodField('get_response')


    def get_response(self, obj):
        try:
            response = obj.get('data')
        except:
            Exception('No character to translate')
        return response

    def get_status_code(self, obj):
        code = '200'
        return code