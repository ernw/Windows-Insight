from misc.constants import CALL_SITE, CALL_STACK_ERROR, CALL_STACK_NO_INFO
class CallStack:
    def __init__(self):
        self.call_stack = []
    
    def parse(self, callstack_data):
        for call in callstack_data.split("\n"):
            if (call.strip()
               and not CALL_SITE in call.lower().strip()
               and not CALL_STACK_ERROR in call.lower().strip() 
               and not CALL_STACK_NO_INFO in call.lower().strip()):
                self.call_stack.append(call.split(" ")[1])

    def get_call_stack(self):
        return self.call_stack

    def get_call_stack_as_string(self):
        return " <- ".join(self.call_stack)

    def __str__(self):
        output = ""
        for call in self.call_stack:
            output += "{}\n".format(call)
        return output

