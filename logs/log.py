#coding=utf-8
import os
import logging
from logging.handlers import TimedRotatingFileHandler
import datetime

#log设置保存路径
log_path = os.path.join("D:/InterfaceTest/",'result')

class Logger(object):
    def __init__(self,logger_name='mylogger'):
        self.logger = logging.getLogger(logger_name)
        #设置log等级
        self.logger.setLevel(logging.DEBUG)
        self.all_log_file_name = 'all.log'   #all.log文件中记录所有的日志信息,日志格式为：日期和时间 - 日志级别 - 日志信息
        self.log_file_name = 'error.log'     #error.log文件中单独记录error及以上级别的日志信息,日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
        self.backup_count = 7
        self.file_output_level = 'ERROR'    #日志输出级别
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   #all.log日志输出格式
        self.errorLog_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s')   #error.log日志输出格式

    def get_logger(self):
        '''在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回'''
        if not self.logger.handlers:
            #记录完整日志 且避免日志重复
            # all.log要求按照时间进行日志切割，因此他需要用logging.handlers.TimedRotatingFileHandler
            console_handler = logging.handlers.TimedRotatingFileHandler(filename=os.path.join(log_path,self.all_log_file_name),when= 'midnight',
                                                                        interval=1,backupCount=7,atTime=datetime.time(0,0,0,0)
                                                                        )
            console_handler.setFormatter(self.formatter)
            self.logger.addHandler(console_handler)
            file_handler = logging.handlers.TimedRotatingFileHandler(filename=os.path.join(log_path,self.log_file_name),when= 'D',
                                                                        interval=1,backupCount=7,atTime=datetime.time(0,0,0,0)
                                                                        )
            file_handler.setFormatter(self.errorLog_formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


if __name__ == '__main__':
    logger = Logger().get_logger()
    logger.debug('debug mesage')
    logger.info('info message')
    logger.warning("this is a waring log")
    logger.error('error message')

