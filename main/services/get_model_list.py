from django.db.models import Q
import pry
class GetModelList():
    def __init__(self, model, page=1, limit=10, sort_dir='desc', sort_field='id', search_dict={}):
        self.page = int(page)
        self.limit = int(limit)
        self.sort_dir = sort_dir
        self.sort_field = sort_field
        self.search_dict= search_dict
        self.model = model

    def call(self):
        self.calculate_limit_offset()
        return self.model.objects.filter(
            self.build_search_filter()
        ).order_by(
            self.sort_param()
        )[self.start_index:self.end_index]

    def sort_param(self):
        param = '-' if self.sort_dir == 'desc' else ''
        return param + self.sort_field

    def calculate_limit_offset(self):
        self.start_index = (self.page - 1) * self.limit
        self.end_index = self.start_index + self.limit
    
    def build_search_filter(self):
        search_filter = Q()
        
        for k, v in self.search_dict.items():
            kwargs = {k+'__icontains':v}
            search_filter |= Q(**kwargs)

        return search_filter