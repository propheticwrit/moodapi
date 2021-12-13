from authentication.models import User


class APIMixin():

    def create(self, request, *args, **kwargs):

        if not request.data['user'] and request.user:
            request.data['user'] = [request.user.id]

        return super(APIMixin, self).create(request, args, kwargs)
