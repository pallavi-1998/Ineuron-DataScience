import logging as lg


class log(object):

    def __init__(self, name, level="DEBUG"):
        self.logger = lg.getLogger(name)
        # self.file = "Log/"+str(name) #changes it to only str(name)
        self.file = str(name)
        self.logger.setLevel(lg.DEBUG)
        self.level = level
        # Creating Formatters
        self.format = lg.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        # Creating Handlers
        # self.file_handler = lg.FileHandler(str(self.file) + '.log') # changing self.file to name 
        self.file_handler = lg.FileHandler(str(self.file) + '.log')


        # Adding Formatters to Handlers
        self.file_handler.setFormatter(self.format)
        # Adding Handlers to logger
        self.logger.addHandler(self.file_handler)
        
        # self.stream_handler = lg.StreamHandler()
        # self.stream_handler.setLevel(lg.DEBUG)

    def get_logger(self):
        return self.logger
