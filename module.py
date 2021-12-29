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
boms.append(BOM("KITCHEN-UTENSIL-HOLDER",[Ingredient("EMPTY CAN(S)", 1), Ingredient("WINE CORK(S)", 30) , Ingredient("HOT GLUE STICK(S)", 1)], "Use HOT GLUE to attach WINE CORKS to the outside of the TIN CAN. \nThe metallic outside of the can should be completely covered in wine corks."))
boms.append(BOM("SCRUNCHIE",[Ingredient("HAIR TIE(S)", 1), Ingredient("FABRIC SCRAP(S)", 1), Ingredient("ROLL(S) OF THREAD", 1)], "Cut the FABRIC to 4\" wide by 20\" long. \nSew it round the HAIR TIE using the THREAD and a needle."))
boms.append(BOM("SKATEBOARD-SWING",[Ingredient("ROPE(S)", 2), Ingredient("SKATEBOARD(S)", 1)], "Drill two holes into the deck of the SKATEBOARD, right next to the trucks. \nLead a ROPE each through the holes. \nTie the ends of the ropes around the set of trucks right next to them. \nNow secure the ropes around a tree in your garden."))
boms.append(BOM("COFFEE-TABLE",[Ingredient("WINE BOTTLE(S)", 3), Ingredient("WOOD BOARD(S)", 1)], "Cut the WOOD BOARD into the desired shape for your tabletop. \nDrill 3 bottleneck-sized holes into the tabletop. \nUse the WINE BOTTLES as feet for your coffee table."))
boms.append(BOM("HANGING-PLANTER",[Ingredient("PLATIC BOTTLE(S)", 1), Ingredient("ROPE(S)", 1)], "Cut a palm-sized window into the side of the PLASTIC BOTTLE. \nOn the same side of the bottle, drill a hole into the neck & bottom of the bottle, and lead the ROPE thorugh the HOLES. \nFill the bottle with soil using the window, \nPlant any seeds you want & hang the planter using the rope."))
boms.append(BOM("TRIVET",[Ingredient("WINE CORK(S)", 16), Ingredient("WOOD BOARD(S)", 1), Ingredient("HOT GLUE STICK(S)", 1)], "Cut all WINE CORKS in half along their long side. (So they can no longer roll) \nCut your WOOD BOARD into the shape of a small baking tray. \nGlue the corks to the board. (Flat sides down)\nNow you can place your hot baking trays, pots and pans on your cork trivet."))
boms.append(BOM("MEMOBOARD", [Ingredient("WOOD BOARD(S)", 1), Ingredient("NAIL(S)", 16), Ingredient("ROLL(S) OF THREAD", 1)], "Place the NAILS along the outside edge of the WOOD BOARD. \nWrap the THREAD around the nails in a random pattern. \nYour new memoboard if complete!"))