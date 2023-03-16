from logger import log 
from collections.abc import Iterable

log_obj = log("list")
lg = log_obj.get_logger()

class Custom_list:
    def __init__(self, lst):
        """
        Initializing list values
        """
        try:
            if type(lst) == list:
                self.lst = lst
                lg.info(f"List object created with value: {lst}")
            else:
                lg.error("Raising exception since list is not passed")
                raise Exception(f"You have not entered a list: {lst}")
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def append_list(self, x):
        """
        This method will append element at the end of the list
        """
        try:
            self.lst = self.lst + list(x)
            lg.info(f"List object appended with value: {x}")
        except Exception as e:
            print(e)
            lg.exception(str(e))
    
    def clear_list(self):
        """
        This method will remove all items from list
        and make it empty list
        """
        try:
            self.lst = []
            lg.info("List object cleared")
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def copy_list(self):
        """
        This method will return a shallow copy of the list.
        """
        try:
            x = self.lst[:]
            lg.info("Created shallow copy of the list")
            return x
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def count_list(self,x):
        """
        This method will return number of occurrences of parameter passed.
        """
        try:
            c=0
            for i in self.lst:
                if x == i:
                    c += 1
            lg.info(f"number of occurrences of parameter {x} in the list: {c}")
            return c
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def extend_list(self,x):
        """
        This method will extend list by appending elements from the iterable.
        """
        try:
            if isinstance(x, Iterable):
                for i in x:
                    self.lst = self.lst + [i]
            else:
                self.lst = self.lst+ [x]
            lg.info(f"List {self.lst} is extended by parameter: {x}")
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def index_list(self, x):
        """
        This method will return the parameter first index
        """
        try:
            for i, j in enumerate(self.lst):
                if x == j:
                    lg.info(f"Parameter: {x} found at position:{i} in the List {self.lst}")
                    return i
            raise Exception(f"Parameter: {x} is not found in the list: {self.lst}")
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def insert_list(self, i, x):
        """
        This method will insert object before index.
        """
        try:
            self.lst = self.lst[0:i] + [x] + self.lst[i:]
            lg.info(f"Parameter: {x} inserted at index:{i} in the List {self.lst}")
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def pop_list(self, i=-1):
        """
        This method will remove and return item at index
        If index is not given it will remove last and return.
        """
        try:
            x = self.lst[i]
            if i == -1:
                self.lst = self.lst[0:-1]
            else:
                self.lst = self.lst[0:i] + self.lst[i+1:]
            lg.info(f"Element: {x} removed from index:{i} in the List {self.lst}")
            return x
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def remove_list(self, x):
        """
        This method will remove first occurrence of parameter.
        """
        try:
            c = self.index_list(x)
            if type(c) == int:
                x=self.pop_list(c)
                lg.info(f"Element: {x} removed from index:{c} in the List {self.lst}")
            else:
                raise Exception(f"Parameter: {x} is not found in the list: {self.lst}")
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def reverse_list(self):
        """
        This method will reverse the list.
        """
        try:
            self.lst = self.lst[::-1]
            lg.info("List is reversed")
        except Exception as e:
            print(e)
            lg.exception(str(e))

    def sort_list(self,rev=False):
        """
        This method will sort list in ascending order if rev parameter is False
        or sort list in descending order if rev parameter is True.
        """
        try:
            i = 0
            while (i < len(self.lst) - 1):
                j = i + 1
                while (j < len(self.lst) - 1):
                    if (self.lst[i] > self.lst[j]):
                        temp = self.lst[i]
                        self.lst[i] = self.lst[j]
                        self.lst[j] = temp
                    j = j + 1
                i = i + 1
            if rev:
                self.reverse_list()
                lg.info("List is sorted in ascending order ")
            else:
                lg.info("List is sorted in descending order ")
        except Exception as e:
            print(e)
            lg.exception(str(e))