A wrapper for encoding Lexical features. Simple handcrafted features helps your sequence to sequence model better tagging and chuncking accuracy even in noisy setting. Extremly helpful in case of social media datasets like twitter, reddit or snapchat

## Run
```
#pip install lexfeatures-SaichethanReddy
from lexfeatures import *
r = encoder("Saichethan M. reddy 170101025")
print(r.encode())
```
