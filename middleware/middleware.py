"""class based middleware - altering Django’s input/output"""


class CheckUserLanguageMiddleware:
    """check use language"""

    def __init__(self, get_response):
        """One-time configuration and initialization"""
        self.get_response = get_response

    def language(self, lang_info):
        """check lang and return it"""
        if "en" in lang_info:
            print('user is using english')
        elif "dk" in lang_info:
            print('user is using danish')
        else:
            print('user is not using english')

    def __call__(self, request):
        """put language into header"""
        # Code to be executed for each request before
        # the view (and later middleware) are called
        self.language(request.headers['Accept-Language'])

        response = self.get_response(request)

        return response
