from brewtiful import create_app
import os
from flask import Flask



# if __name__=='__main__':
#     napp=create_app()
#     napp.run(debug=True)

# Use Heroku-assigned port or default to 5000 for local development
# port = int(os.environ.get("PORT", 5000))

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=port)

from brewtiful import create_app

app = create_app()

if __name__ == '__main__':
    # Use Gunicorn as the server for production
    import os
    from gunicorn.app.base import BaseApplication

    class StandaloneApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super(StandaloneApplication, self).__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key, value)

        def load(self):
            return self.application

    options = {
        'bind': '0.0.0.0:5000',
        'workers': 4  # Adjust the number of workers based on your needs
    }

    StandaloneApplication(app, options).run()
