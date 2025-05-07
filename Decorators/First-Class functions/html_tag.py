def html_tag(tag: str):

    def tag_wrapper(message: str):
        return f"<{tag}>{message}</{tag}>"
    
    return tag_wrapper


#==============================================
# Higher order function(or also called closure)
# Function that returns a function
#==============================================

h1 = html_tag("h1")
print(h1("Closures in Practice"))

h2 = html_tag("h2")
print(h2("Wrap the message into html tags"))

p = html_tag("p")
print(p("Using the concept of first-call functions, higher-order functions, and closures one can write a program to ...."))