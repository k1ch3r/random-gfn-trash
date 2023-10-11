# # als i in range mit step

# for i in range(0, 201, 2):
#     geradeZahlenStep = []
#     geradeZahlenStep.append(i)
#     print(geradeZahlenStep)


# # mit modulo

# for i in range(0, 201):
#     if i % 2 == 0:
#         geradeZahlenModulo = []
#         geradeZahlenModulo.append(i)
#     print(geradeZahlenModulo)


#kompakt in global scope

geradeZahlenGlobaleVar = list(range(0, 201, 2))
print(geradeZahlenGlobaleVar)