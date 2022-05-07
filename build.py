from pathlib import Path
Path("output").mkdir(exist_ok=True)

font = fontforge.open('TF2C.sfd')
font.generate('output/TF2C.ttf')
font.generate('output/TF2C.woff')
font.generate('output/TF2C.woff2')
font = fontforge.open('TF2CBuild.sfd')
font.generate('output/TF2CBuild.ttf')
font.generate('output/TF2CBuild.woff')
font.generate('output/TF2CBuild.woff2')
font = fontforge.open('TF2CProfessor.sfd')
font.generate('output/TF2CProfessor.ttf')
font.generate('output/TF2CProfessor.woff')
font.generate('output/TF2CProfessor.woff2')
font = fontforge.open('TF2CSecondary.sfd')
font.generate('output/TF2CSecondary.ttf')
font.generate('output/TF2CSecondary.woff')
font.generate('output/TF2CSecondary.woff2');