import pry

class BaseController():
    def call(self, request, *args, **kwargs):
        self.request = request
        return {
            'POST' : self.create,
            'PATCH' : self.update,
            'GET' : self.fetch,
            'DELETE' : self.delete
        }.get(request.method)(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass

    def index(self, request, *args, **kwargs):
        pass

    def fetch(self, request, *args, **kwargs):
        if(len(kwargs) > 0):
            return self.get(request, *args, **kwargs)
        else:
            return self.index(request, *args, **kwargs)
        