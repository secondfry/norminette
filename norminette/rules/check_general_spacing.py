from rules import Rule


class CheckGeneralSpacing(Rule):
    def __init__(self):
        super().__init__()
        self.depends_on = [
            "IsDeclaration",
            "IsControlStatement",
            "IsExpressionStatement",
            "IsAssignation",
            "IsFunctionCall",
        ]

    def run(self, context):
        """
            Checks for tab/space consistency
        """
        i = context.skip_ws(0)
        while i < context.tkn_scope:
            if context.check_token(i, "TAB") is True:
                context.new_error("TAB_INSTEAD_SPC", context.peek_token(i))
                break
            if context.check_token(i, "NEWLINE") is True:
                i = context.skip_ws(i, nl=True)
            i += 1
        return False, 0
