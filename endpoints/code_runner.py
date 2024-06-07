from RestrictedPython import compile_restricted, safe_builtins
from RestrictedPython.Guards import guarded_iter_unpack_sequence

DEFAULT_CODE = """
def move(data):
  # Tu codigo aqui
  # Debes devolver "up", "down", "left" o "right"

  board = data["board"]
  you = data["you"]

  return "left"
"""

# Define a restricted execution namespace
restricted_globals = {'__builtins__': {}}

restricted_globals = {
    "__builtins__": safe_builtins,
    "__import__": lambda name, globals=None, locals=None, fromlist=(), level=0: __import__(name),
    # "getattr": lambda obj, attr: getattr(obj, attr),
    '_getattr_': getattr,  # Allow attribute access
    "_iter_unpack_sequence_": guarded_iter_unpack_sequence,
    "_getiter_": iter,
    '_getitem_': lambda obj, key: obj[key]  # Allow indexing
}

def compile(user_code):
    # Compile the user-provided code in a restricted environment
    compiled_code = compile_restricted(user_code, '<user_code>', 'exec')

    # Execute the compiled code within the restricted globals
    exec(compiled_code, restricted_globals)

    # Get the function from the restricted globals
    move_function = restricted_globals.get('move')

    # Check if the function is callable
    if callable(move_function):
        # Call the function with the provided arguments
        return move_function
    else:
        raise ValueError("User code does not define a callable function named 'move'")
