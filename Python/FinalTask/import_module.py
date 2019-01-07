""" Module import example. """
from tag_counter import TagCounter
# Hold simple HTML Example
html_example = """\
    <html>
      <head>
        <title>Count HTML Tags sample </title>
      </head>
      <body>
        <IMG SRC="">
        <bgsound src="">
        <a></a>
        <span></span>
        <a></a>
        <span>
          <IMG SRC="">
          <IMG SRC="">
          <a></a>
        </span>
        <span>
          <a></a>
        </span>
      </body>
    </html>
    """

cls_count = TagCounter()

print(cls_count.count('url', 'https://www.google.com'))

# Enable logging to file
cls_count.config_log(['file', 'log_file.log'])
print(cls_count.count('url', 'https://ya.ru'))
print(cls_count.count('html', html_example))

# Enable logging to aws
cls_count.config_log(['aws', 'log_file.log'])
print(cls_count.count('file', 'html_file.html'))

# Disable logging and print example
cls_count.config_log(['Disabled', 'log_file.log'])
print('Plain text Html example:\n', html_example)
print(cls_count.count('html', html_example))
