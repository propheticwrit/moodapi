


class APIMixin():

    def get_queryset(self):

        queryset = self.queryset

        params = self.request.query_params

        if 'subject' in params:
            queryset = queryset.filter(user__subject=params['subject'])

        return queryset
