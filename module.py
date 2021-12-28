#Ingredient - combines the name of a material with a corresponding quantity
#           - appers either as a component of a BOM or as a component of the user's inventory
class Ingredient:
    def __init__(self, name = "", quantity = 0):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return str(self.quantity) + " " + str(self.name)

#BOM(Bill of Materials) - describes what materials are needed to craft the named item 
class BOM:
    def __init__(self, name = "", ingredients = [], instructions = ""):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions + "\n"

    def __str__(self):
        result = self.name + ":\n"
        for Ingredient in self.ingredients:
            result += str(Ingredient) + "\n"
        return result
    
    def printInstructions(self):
        print(self.instructions)

def match(bom, inventory = {}):
    anymatch = False
    missingitems = []
    for Ingredient in bom.ingredients:
        for item in inventory:
            if item == Ingredient.name:
                if int(inventory[item]) != 0:
                    anymatch = True
                if Ingredient.quantity > int(inventory[item]):
                    missingitems.append(str(Ingredient.quantity - int(inventory[item])) + " " + Ingredient.name)
    if anymatch == False:
        return ""
    if len(missingitems) == 0:
        return bom.name + " - you have all necessary items.\nType \"show " + bom.name +  "\" to learn how to build a(n) " + bom.name + "\n\n"
    result = bom.name + " - but in addition to what you already have, you need:\n"
    for item in missingitems:
        result += item + "\n"
    result += "Type \"show " + bom.name +  "\" to learn how to build a(n) " + bom.name + "\n\n"
    return result


#list of all available bills of materials
boms = []
boms.append(BOM("CHAIR",[Ingredient("BOARD(S)", 1), Ingredient("STICK(S)", 3)], "(INSTRUCTIONS FOR CHAIR)"))
boms.append(BOM("TABLE", [Ingredient("BOARD(S)", 1), Ingredient("STICK(S)", 4)], "(INSTRUCTIONS FOR TABLE)"))
boms.append(BOM("MEMOBOARD", [Ingredient("BOARD(S)", 1), Ingredient("NAIL(S)", 16), Ingredient("STRING(S)", 1)], "(INSTRUCTIONS FOR MEMOBOARD)"))