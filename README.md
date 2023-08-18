# QuickLogger-Python
QuickLogger is a simple logger class in Python.

## Usage
### Syntax
    class QuickLogger {
        /* Methods */
        log(
            loggingLevel = <"OFF" | "FATAL" | "ERROR" | "WARN" | "INFO" | "DEBUG" | "TRACE" | "ALL">, 
            String message)
        error(String message)
         warn(String message)
         info(String message)
        debug(String message)

        QuickLogger([String logFilename , String loggingLevel, boolean hasDateTime])
    }

### Paramenters
**format**
- standard Python text formatting - example: https://docs.python.org/3/tutorial/inputoutput.html

**logFilename**
- Specifies the path and filename for where the logging will be done. If none, it will log to standard & error output.

**hasDateTime**
- If the output should show timestamp or not. Default: true


## Examples
  - Declaration: 
    - This will write to a file
  
      `LOG = QuickLogger("/opt/log/application.log", "INFO");`

    - This will write to the standard output

      `LOG = QuickLogger(None, "INFO");`

  - Usage:
 
        LOG.info("Connection details: Host: %s, User: %s. Port: %d" % (host, user, port));
        LOG.error("Fatal error! Exiting...");
