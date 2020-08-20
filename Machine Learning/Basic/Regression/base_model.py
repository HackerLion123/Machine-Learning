import logging



class BaseModel(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    
    def train(self, data, accuarcy=["f1-score", "mape"]):
        """
            TODO:
            1] Split the model into train and test
            2] train a model based on training data.
            3] Calcuate the accuracy of the model on train data and return it.
        """
        raise NotImplementedError("Function is not implemented or not applicable for this model")

    def test(self, data):
        """
            TODO:
            1] Using the model predict the values
            2] Calculate the accuaracy of the precitions
            3] explain predcitions
        """

        raise NotImplementedError("Function is not implemented or not applicable for this model")

    def predict(self, input, explain=True):
        raise NotImplementedError("Function is not implemented or not applicable for this model")

    def _accuarcy(self, method=[]):
        pass

    def _explain_predictions(self):
        """
            Choose the steps that are applicable to this model and do those steps in this function
        """
        pass



    
