msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
""" # .format(name="Justin", website='cfe.sh') without using the function

def format_msg(my_name="Dev tez", my_website="t&tinc.org"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg 