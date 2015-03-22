import os
from PIL import Image

for d, f, r in os.walk("icons"):
	for filename in f:
		print filename