class LoggingMiddleware:
    def __init__(self, get_response):
        # One-time configuration and initialization

    def __call__(self, request):
        """
        Method to put output including error in a middleware formatting the output in Json Format
        :param request:
        :return retrieve the response/request most representative information to terminal
        """

        response = self.get_response(request)
        logged_data = {
            'response_status_code' : response.status_code,
            'response_content' : response.content,
            'requested_url' : request.path,
            'requested_method' : request.method,
            'requested_data' : request.POST

        }
        print(logged_data)
        return response