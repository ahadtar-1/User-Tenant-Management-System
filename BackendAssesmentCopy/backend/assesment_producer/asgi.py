import uvicorn
import pydantic
from app.main import app

if __name__ == "__main__":
	print('compiled:', pydantic.compiled) # Put this in some debug logging
	uvicorn.run(app, host="0.0.0.0", port=5050)
