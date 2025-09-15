# Fixed version: skip 'c', 'm', 'E' as language names
m = 2.0   # kg
c = 3.0   # m/s

languages = [
    "python", "java", "scala", "cpp", "csharp", "go", "rust", "swift",
    "kotlin", "ruby", "php", "perl", "lua", "haskell", "ocaml", "fsharp",
    "erlang", "elixir", "julia", "r", "matlab", "octave", "fortran", "pascal",
    "ada", "dart", "vb", "scheme", "lisp", "clojure", "commonlisp", "prolog",
    "smalltalk", "bash", "powershell", "typescript", "javascript", "coffeescript",
    "nim", "crystal", "vala", "d", "zig", "assembly", "scratch", "logo", "awk",
    "sed", "tcl", "postscript", "forth", "apl", "j", "k", "wolfram", "maxima",
    "sml", "ml", "mercury", "cobol", "abap", "delphi", "objectivec", "solidity",
    "vhdl", "verilog", "systemverilog", "plsql", "sql", "foxpro", "groovy",
    "coldfusion", "actionscript", "elm", "purescript", "reasonml", "idris",
    "agda", "coq", "chapel", "pony", "factor", "rebol", "red", "ocelot",
    "qsharp", "x10", "modula2", "oberon", "eiffel", "simula", "bcpl", "algol",
    "snobol", "icon", "rex", "rexx", "harbour", "clipper"
]

for lang in languages:
    globals()[lang] = 1
    E = globals()[lang] * (m * c**2)
    print(f"E = {lang} * m * c**2  =>  E = {E} J")
