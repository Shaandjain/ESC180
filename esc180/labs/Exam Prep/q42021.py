def unlock(input):

   unlock.history = []
   unlock.history.append(input)

   if len(unlock.history)>4:
      unlock.history.pop(0)

   if unlock.history == ["fall", "costumes", "costumes", "pumpkin"]:
      return "Unlocked"
   else:
      return "Locked"
print(unlock("fall"))
print(unlock("costumes"))
print(unlock("costumes"))
print(unlock("pumpkin"))
print(unlock.history)


s = "waffle"
print(s.upper())