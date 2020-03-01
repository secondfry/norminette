from lexer import Token
from rules import PrimaryRule


class CheckVarDeclarations(PrimaryRule):
    def __init__(self):
        super().__init__()
        self.priority = 10

    def assignment_right_side(self, context, pos):
        sep = ["COMMA", "SEMI_COLON", "ASSIGN"]
        i = self.skip_ws(context, pos)
        lbrackets = ["LBRACE", "LPARENTHESIS", "LBRACKET"]
        rbrackets = ["RBRACE", "RPARENTHESIS", "RBRACKET"]
        while context.check_token(i, sep) is False:
            if context.check_token(i, lbrackets) is True:
                i = self.skip_nest(context, i)
            i += 1
        return True, i

    def var_declaration(self, context, pos):
        ret, i = self.check_identifier(context, pos)
        if ret is False:
            return ret, pos

        pclose = ["RPARENTHESIS", "NEWLINE", "SPACE", "TAB"]
        i += 1
        while context.check_token(i, pclose):
            i += 1
        i = self.skip_brackets(context, i)
        while context.check_token(i, pclose):
            i += 1
        if context.check_token(i, "ASSIGN") is True:
            i += 1
            ret, i = self.assignment_right_side(context, i)
            if ret is False:
                return False, pos
        if context.check_token(i, "SEMI_COLON") is True:
            return True, i
        if context.check_token(i, "COMMA") is True:
            i += 1
            return True, i
        return False, pos

    def run(self, context):
        ret, i = self.check_type_specifier(context, 0)
        if ret is False:
            return False, 0

        ret, i = self.var_declaration(context, i)
        if ret is False:
            return False, 0
        while ret:
            ret, i = self.var_declaration(context, i)
            if context.check_token(i, "SEMI_COLON") is True:
                break
        else:
            return False, 0
        i += 1
        return True, i
