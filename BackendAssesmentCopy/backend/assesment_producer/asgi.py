import uvicorn
import pydantic
from app.main import app
from utils.producer import producer

if __name__ == "__main__":
    print("compiled:", pydantic.compiled)  # Put this in some debug logging
    # print(producer.bootstrap_connected(), flush=True)
    uvicorn.run(app, host="0.0.0.0", port=5030)
