import os
from utils import *

messages = []
setup_args()

print('running')

for message in run_training('./training/richard/train.yaml'):
    print(message)
    messages.append(message)