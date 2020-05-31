# google-form-filler-python

## installing
```bash
pip install googleform
```

## usage

```python
import googleform
gform = googleform.get('https://docs.google.com/forms/d/1jzDkEha066GwSCcSrCg1yaJJLpJAk0_aIFwf6GQgmmU/viewform')

# get information from  
gform.questions[0].title # "Check boxes"
gform.questions[0].options #  ['Option 1', 'Option 2', 'Option 3']

# fill the questions
gform.questions[0].answer('Option 1')
gform.questions[0].answer('Option 2')

# send it out
gform.submit()

# if a form has multiple pages use .next()
page_2 = gform.next()
page_2.questions[0].answer("my answer")
page_2.submit()
```