# What is the main purpose of a decorator in Python?
# To wrap a function and extend/modify its behavior without changing its source


# What does functools.wraps do when used inside a decorator?
# It preserves the original function's metadata (name, docstring, signature)


# What is the output of the following code?
def upper(f):
  def w():
    return f().upper()
  return w

def exclaim(f):
  def w():
    return f() + "!"
  return w

@upper
@exclaim
def say():
  return "hi"

print(say())
#HI!
