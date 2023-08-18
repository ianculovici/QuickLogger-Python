import datetime

class QuickLogger:
    output = None
    def __init__(self, logfile=None, level="WARN", includeDate=True):
        self.logLevels = ["OFF", "FATAL", "ERROR", "WARN", "INFO", "DEBUG", "TRACE", "ALL"]
        self.set_level(level)
        self.includeDate = includeDate
        if logfile:
            self.output = open(logfile, "a")

    def close(self):
        if self.output:
            self.output.close()

    def log(self, level, message):
        if not level in self.logLevels:
            message = "INVALID LEVEL: " + level + "   " + message
            level = "ERROR"
        log_message = ("%-5s" % (level)) + ": " + message
        if self.includeDate:
            log_message = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} - {log_message}"
            if self.logLevels.index(level) <= self.logLevels.index(self.LEVEL):
                if self.output:
                    self.output.write(log_message + "\n")
                    self.output.flush()
                else:
                    print(log_message)

    def set_level(self, level):
        if level in self.logLevels:
            self.LEVEL = level
        else:
            print("Invalid log level")

    def get_level(self):
        return self.LEVEL

    def debug(self, message):
        self.log("DEBUG", message)

    def info(self, message):
        self.log("INFO", message)

    def warn(self, message):
        self.log("WARN", message)

    def error(self, message):
        self.log("ERROR", message)
