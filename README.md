# serverHttp-clientBrowser
    2 applications on the HTTP protocol, server Http consists of a page delivery server and client Browser is a server access, pageview and dowload application.

    All applications were developed in python using the socket API.


# Requirements
    Python from version 2+ available at: (https://www.python.org/).

# How to use
    - server.py
    
        
        ```bash
        $ bash install.sh
        ```
    
        To use in the terminal with browser.py or browser from operational system
        ```bash
        $ bash python server.py mod-brower 8080
        ```
        To use in other forms
        ```bash
        $ python server.py path_file 8080
        ```

    - browser.py
        To use in terminal
        ```bash
        $ python browser.py 0.0.0.0/path_file port
        ```

# Responses
    - 0.0.0.0/test/
    For folder path it will return a list of files inside the folder

    - 0.0.0.0/test/index.html
    For file path will return the contents of the file and download to the download folder

    - 0.0.0.0/test/not-file.html
    For the file path that does not exist it will return an error message and error code 404

