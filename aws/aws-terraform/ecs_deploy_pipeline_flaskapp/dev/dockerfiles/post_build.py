import shlex
import subprocess
import os
import json

import main_build

image_def = [
    {"name": "app", "imageUri": "{}:latest".format(main_build.REPO_APP)},
    {"name": "web", "imageUri": "{}:latest".format(main_build.REPO_WEB)}
]

with open('imagedefinitions.json', 'w') as f:
    json.dump(image_def, f)
    
