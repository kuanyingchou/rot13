import webapp2
import cgi

form = '''
<form method="post">
  <textarea name="text" rows="5">%s</textarea>
  <br>
  <input type="submit">
</form>
'''
def rot13_char(c):
    if not c.isalpha():
        return c
    idx = ord(c)
    if idx >= ord('A') and idx <= ord('Z'):
        base = ord('A')
    elif idx >= ord('a') and idx <= ord('z'):
        base = ord('a')
    else:
        print c
        return c
    i = idx - base

    o =  chr(base + ((i + 13) % 26))
    # print c, '->', o
    return o

def rot13(text):
    res =  ''.join(rot13_char(c) for c in text)
    # print res
    return res

class MainPage(webapp2.RequestHandler):
    def write_form(self, form, text):
        self.response.write(form % cgi.escape(text))


    def get(self):
        self.write_form(form, '')

    def post(self):
        # self.response.write(self.request)
        # self.response.write('<br>')
        user_text = self.request.get('text')
        text = rot13(user_text)
        self.write_form(form, text)


app = webapp2.WSGIApplication([ ('/', MainPage), ], 
        debug=True)
