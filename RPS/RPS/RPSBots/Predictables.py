import random, time

winningMoves = {"R" : "P", "P" : "S", "S" : "R"}
def getMove():
	offset = random.randint(1,16)
	randBase = "AJgkxexbBeJq09DgHhSfW36Mb39ObkiMVNE6a9OUznueKy813sdrtIWuxCfs87IjqirAWXhsNrl1mbtXyWNXZQVz5feHj6RftSPysbRphQzgv5Z3ydItdGldaDHoYTBkg8GN8nAM36S0FT6OBtzEvTF23hVeSbybyISeoy1lC6KNWw5zbZ4fAQsUDVZEJ0jlnqi9B6j8muA91YhOsQpxuIXoFvRthxyalzFOoZ28XYAG1YBV4M678GH47r7xxEVtjFTVJ0nFBiOH8dDg4uFBgW57F6GfU2MZPpaiEaUpSWDB7b9CqpIHhfRGCMxgjFAyYryyJW4NkBo9A7pDKxmbjT8wrG0U0kmhFh3sBxmvjjBZYFfYIWeiKuuUYrFatW6JveQjcavqoXMkBTvWqRv8l7rsGO1GQe70mNYS1yTkNQKdfaGkNbKzh7YCco7PSZSR5nlvJK1eE2vA6gTBqiuDIQnHrKwXiUi5b8G4ccSNrgk2ftgdfKd9"
	seed = ""
	for temp in randBase:
		seed += chr(ord(temp)+offset)
	random.seed(seed)
	return winningMoves[random.choice(previousMoves)]
if input!="":
	previousMoves.append(input)
else:
	previousMoves = ["R", "P", "S"]
output = getMove()