from lexer import Token
from rules import PrimaryRule
from context import GlobalScope, UserDefinedType, ControlStructure, Function


class IsComment(PrimaryRule):
    def __init__(self):
        super().__init__()
        self.priority = 25
        self.scope = []

    def run(self, context):
        """
            Catches comments tokens
        """
        i = context.skip_ws(0)
        if context.check_token(i, ["MULT_COMMENT", "COMMENT"]) is True:
            i += 1
            i = context.eol(i)
            return True, i
        return False, 0
