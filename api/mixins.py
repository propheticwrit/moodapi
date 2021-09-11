from authentication.models import User


class APIMixin():

    def get_queryset(self):

        queryset = self.queryset

        if self.request.user:
            queryset = queryset.filter(user=self.request.user)

        return queryset

    def create(self, request, *args, **kwargs):

        if request.user:
            request.data['user'] = [request.user.id]

        return super().create(request, args, kwargs)
