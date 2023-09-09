import imgkit
from html2image import Html2Image
hti = Html2Image()

def formatContent(content):
    formattedContent = """
        <html>
          <head>
            <meta name="imgkit-format" content="png"/>
            <meta name="imgkit-orientation" content="Portrait"/>
          </head>
         <h2> 割れる </h2>
        </html>
    """

    return str(formattedContent)

#imgkit.from_string(str(formatContent), "output.jpg")

css = "h2 {font-size: 80px; text-align: center}"
formattedContent = """
<html>
    <head>
    </head>
    <h2> 割れる </h2>
</html>
"""

hti.screenshot(html_str=formattedContent, css_str=css, save_as='red_page.png')
