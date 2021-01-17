import inspect
import harmony.models._models as m

used = []
for name, _ in inspect.getmembers(m, inspect.isclass):
    if name.endswith('Parameters') or name.endswith('Request') or name.endswith('Response'):
        used.append(name)

o_h = "TOP_LEVEL_MODELS = (\n"
o = ",\n".join(["    {}".format(n) for n in used])
o_e = "\n)"

with open("models.txt", 'w') as mf:
    mf.write(o_h + o + o_e)