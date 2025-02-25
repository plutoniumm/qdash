## qdash

### Usage

```bash
pip install -r requirements.txt
python index.py
```

### Modifying
Basic logging features have already been added. Please add more accordingly. The dev should be able to reconstruct the chain of events that led to the error for a given crash.

External CSS:
```py
# add the file to assets and import it
gr.Blocks(css=CSS("file.css"))
```

External JS:
```py
# add the file to assets and import it
gr.Blocks(js=JS("file.js"))
# allowed js, mjs, cjs, ts
```

Google Analytics:
```py
# add the tracking id
gr.Blocks(head=GA("UA-123456789-1"))
```

Adding Auth:
```py
# add the username and password
demo.launch(auth=("username", "password"))
# OR for multiple users
demo.launch(auth=[("username1", "password1"), ("username2", "password2")])
```