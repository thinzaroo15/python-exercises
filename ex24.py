print("Let's practice everying .")
print('You\'d need to know \' about escapes with \\that do:')
print('\n newlines and \t tabs')
poem="""\t The lovely world wit logic so firmly planted cannot discern \n the needs of love nor comprehend passiion form intuition and requires and explanation \n\t\twhere there is none."""
print("------------------------")
print(poem)
print("------------------------")
five = 10 -2+3-6
print(f"This should be five :{five}")
def decret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/ 100
    crates = jars/100
    return jelly_beans,jars,crates
start_point =10000
beans,jars,crates = decret_formula(start_point)
print("with a staring point of:{}".format(start_point))
print(f"We'have {beans} beans,{jars}jars,and {crates} crates")
start_point =start_point /10
print("We can also do that this way:")
formula = decret_formula(start_point)
print("WE'd have {} beans,{}jars,and {}crates".format(*formula))
