import uvicorn
import pydantic
import sys
import asyncio
import threading
from threading import Thread
from app.main import app
import utils.consumer as consumer 
	

def FuncTwo():
	print('Consumer Started:', flush=True)	
	consumer.consume_events()

if __name__ == "__main__":
	thread_one = Thread(target=FuncTwo,daemon=True)
	thread_one.start()
	uvicorn.run(app, host="0.0.0.0", port=5020)





