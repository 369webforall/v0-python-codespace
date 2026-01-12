print("We are learning if elif and else")

# if, elif and else

if True:
    print("code will here when true")

if False:
    print("This code will not run")

age = 17

if age > 18:
    print("You allow for voting")
else:
    print("You are under age")


nonsense = "blog trust fund tattooed williamsburg poke roof party"
has_ok = "pi" in nonsense

if has_ok:
    print("yeet")
elif len(nonsense) > 10:
    print("yo")
else:
    print("no")

has_zoo = "zoo" in nonsense
has_fun = "fun" in nonsense

if has_zoo and has_ok:
    print("cool")
elif has_ok:
    print("rad")
elif has_fun:
    print("dope")
else:
    print("nope")

