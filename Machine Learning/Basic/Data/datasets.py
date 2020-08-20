import pandas as pd
import requests
import kaggle
import os


class LoadDataset(object):

    def __init__(self, url=None):
        self.url = ""

    

    def get_data(self):
        pass
    
    def _get_url_type(self):
        pass

    def _fetch_data(self):
        pass

    def _get_info(self):
        pass


class TitanicDataset(LoadDataset):

    def __init__(self):
        pass

class WineReviewsDataset(LoadDataset):

    def __init__(self):
        pass

if __name__ == "__main__":
    pass