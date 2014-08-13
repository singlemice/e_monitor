__author__ = 'lihongchao'
import ConfigParser

class ReadConfig():
    def __init__(self):
        self.config=ConfigParser.ConfigParser()
        self.config.read('config.cfg')
    def ReadSection(self,section):
        dict={}
        options=self.config.options(section)
        for option in options:
            try:
                dict[option]=self.config.get(section,option)
            except:
                print("exception on %s" % (option))
                dict[option] = None
        return dict


if __name__=="__main__":
    rc=ReadConfig()
    dic=rc.ReadSection('redis')
    print dic
