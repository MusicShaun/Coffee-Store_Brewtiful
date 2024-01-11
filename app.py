from brewtiful import create_app
import os
from flask import Flask

# if __name__=='__main__':
#     napp=create_app()
#     napp.run(debug=True)

app = Flask(__name__)

# Use Heroku-assigned port or default to 5000 for local development
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)