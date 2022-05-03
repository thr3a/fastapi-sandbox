from fastapi import FastAPI
import mpd

app = FastAPI()
client = mpd.MPDClient()
client.connect("linode.turai.work", 6600)

@app.get("/")
async def hello():
  return {"message": "hello world!"}
