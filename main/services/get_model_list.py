class GetModelList():
    def __init__(self, model, page=1, entry_per_page=10, sort_dir='desc', sort_field='id', search_dict={}):
        self.page = page
        self.entry_per_page = entry_per_page
        self.sort_dir = sort_dir
        self.sort_field = sort_field
        self.search_dict=search_dict
        self.model = model

    def call(self):
        self.calculate_limit_offset()
        return self.model.objects.filter(
            **self.search_dict
        ).order_by(
            self.sort_param()
        )[self.start_index:self.end_index]

    def sort_param(self):
        param = '-' if self.sort_dir == 'desc' else ''
        return param + self.sort_field

    def calculate_limit_offset(self):
        self.start_index = (self.page - 1) * self.entry_per_page
        self.end_index = self.start_index + self.entry_per_page