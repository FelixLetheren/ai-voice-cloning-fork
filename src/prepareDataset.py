import os
from utils import *

messages = []
setup_args()
	
message = transcribe_dataset( voice="richard", language="en", skip_existings=False, progress=None )
messages.append(message)

message = prepare_dataset( voice="richard", use_segments=False, text_length=12, audio_length=1, progress=None )
messages.append(message)
