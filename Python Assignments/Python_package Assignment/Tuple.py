from logger import log 
import random
from collections.abc import Iterable

log_obj = log("tuple")
lg = log_obj.get_logger()

class Custom_tuple:
    def __init__(self,t):
        """
        Initializing tuple values
        """
        try:
            if type(t) == tuple:
                self.t=t
                lg.info(f"Tuple object created with value: {t}")
            else:
                lg.error("Raising exception since tuple is not passed")
                raise Exception(f"You have not entered a tuple: {t}")
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def count_tuple(self,x):
        """
        This method will return number of occurrences of parameter passed.
        """
        try:
            c=0
            for i in self.t:
                if x == i:
                    c += 1
            lg.info(f"number of occurrences of parameter {x} in the tuple: {c}")
            return c
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def index_tuple(self, x):
        """
        This method will return the parameter first index
        """
        try:
            for i, j in enumerate(self.t):
                if x == j:
                    lg.info(f"Parameter: {x} found at position:{i} in the Tuple {self.t}")
                    return i
            raise Exception(f"Parameter: {x} is not found in the tuple: {self.t}")
        except Exception as e:
            print(e)
            lg.exception(str(e))
