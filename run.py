from whiningapp.settings import web_host_address, web_host_port
from whiningapp.whining import app

app.run(host=web_host_address, port=web_host_port)
