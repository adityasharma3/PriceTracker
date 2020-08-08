# PriceTracker

A simple python script that alerts users when a certain products price below their budget by sending out an email.


## Installing dependencies
```bash
    pip install -r requirements.txt
```

```python
    python app.py
```
---
in this script , the example of iphone 11 has been taken and if to be used , user can modify the url and the user email.

```python
    url = 'https://www.amazon.in/Apple-iPhone-11-64GB-Black/dp/B07XVMDRZY?ref_=Oct_DLandingS_D_2f2e560d_60&smid=A14CZOWI0VEHLG'
```

```python
     server.sendmail (
        'aditya09test@gmail.com' , 
        #Your email , 
        message 
    )
```
