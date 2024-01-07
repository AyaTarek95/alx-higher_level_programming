#!/usr/bin/python3
"""script that takes in a URL
sends a request to the URL
displays the body of the response
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as er:
        print("Error code: {}".format(er.code))
