# Django Ecommerce

## References for This Project

- [https://github.com/codingforentrepreneurs/eCommerce](https://github.com/codingforentrepreneurs/eCommerce)
- [YouTube PlayList](https://www.youtube.com/watch?v=fhATkPoU22k&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK)

## Related Python Packages

- Global `pip install`
  - virtualenv
- virtual enviroment `pip install`
  - django (2.1.3): pip install django==2.1.3
  - mysqlclient [download from](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
  - pillow (for ImageField)

## MySQL Connection

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database name>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET innodb_strict_mode=1',
            'sql_mode': 'STRICT_TRANS_TABLES',
            'charset': 'utf8mb4'
        }
    }
}
```

## Other Resources

- [Bootstrap](https://getbootstrap.com/)
- [JQuery Download](https://jquery.com/download/)
- [popper.js Download](https://github.com/FezVrasta/popper.js#installation)
