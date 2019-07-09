def parse_response(response):
    try:
        return response.split(",", 1)
    except:
        new_input = raw_input("Please enter a valid comma seperated number choice.")
        parse_response(new_input)
