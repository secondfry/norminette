failed_tokens_tests = {
    #   String to test as key: error position as value
    "\tdouble f=45e++ai": [1, 14],
    "\tchar *b = \"e42\n\n": [1, 15],
    "int\t\t\tn\t= 0x1uLl;": [1, 19],
    "char\t\t\t*yo\t\t\t= \"": [1, 31],
    "{return 1;}\\\\\\n": [1, 12],
    "int a = a+++++a;\ndouble b = .0e4x;": [2, 12],
    "int a = 1;\nint b = 10ul;\nint c = 10lul;\n": [3, 9],
    "int number = 0x1uLl;": [1, 14],
    "int number = 0x1ULl;": [1, 14],
    "int number = 0x1lL;": [1, 14],
    "int number = 0x1Ll;": [1, 14],
    "int number = 0x1UlL;": [1, 14],
    "int number = 10ullll": [1, 14],
    "int number = 10lul": [1, 14],
    "int number = 10lUl": [1, 14],
    "int number = 10LUl": [1, 14],
    "int number = 10uu": [1, 14],
    "int number = 10Uu": [1, 14],
    "int number = 10UU": [1, 14],
    "int number = 0b0101e": [1, 14],
    "int number = 0b0101f": [1, 14],
    "int number = 0b0X101f": [1, 14],
    "int number = 0X101Uf": [1, 14],
    "int number = 0101f": [1, 14],
    "float number=10.12fe10": [1, 14],
    "float number=10.fU": [1, 14],
    "float number=21.3E56E4654": [1, 14],
    "float number=105e4d": [1, 14],
    "float number=105flu": [1, 14],
    "float number=105fu": [1, 14],
    "float number=105eu": [1, 14]
}
