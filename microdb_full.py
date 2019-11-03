import pickle


class MicroDB:

    def load(self):
        db_file = open('d', 'rb')
        loaded_object = pickle.load(db_file)
        self.__dict__ = loaded_object.__dict__

    def __setattr__(self, key, value):
        super(MicroDB, self).__setattr__(key, value)
        db_file = open('d', 'wb')
        pickle.dump(self, db_file)
