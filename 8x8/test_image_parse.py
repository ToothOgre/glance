import os
from PIL import Image

for d, r, f in os.walk("icons\"):
	for filename in f:
		print filename