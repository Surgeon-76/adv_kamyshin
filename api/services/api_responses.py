
class PaginationsResponses:
    def __init__(self, total, page, page_size, results) -> None:
        self.total = total
        self.page = page
        self.page_size = page_size
        self.results = results

    @property
    def get_responses(self):
        next_page = self.page + 1
        prev_page = self.page - 1
        if self.page == 1:
            prev_page = None
        if self.page == round(self.total/self.page_size):
            next_page = None

        response = {
            'total': self.total,
            'count': round(self.total/self.page_size),
            'prev_page': prev_page,
            'next_page': next_page,
            'results': self.results,
        }

        return response
        # json_compatible_item_data = jsonable_encoder(response)
        # return JSONResponse(
        #     status_code=200,
        #     content=json_compatible_item_data
        # )
