#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df= pd.read_excel(r"zip_code_database.xlsx")


# In[2]:


# df.head()


# In[3]:


from flask import Flask, request, render_template_string
app = Flask(__name__)
HTML = '''
    <html>
        <body>
            <form method="post" action="/">
                <input type="text" name="number" placeholder="Enter a number" />
                <input type="submit" value="Get Input Format" />
            </form>
            {% if result %}
            <h2>Result: {{ result }}</h2>
            {% endif %}
        </body>
    </html>
'''


# In[4]:


#Start
print("start")


# In[5]:


def format_city_name(city_name, state_suffix):
    # Split the location by spaces
    parts = city_name.split()
    # If there's more than one word, join them with a hyphen
    if len(parts) > 1:
        # Convert to lowercase and add the state suffix
        return '-'.join(parts).lower() + state_suffix
    # If it's a single word, leave it as is and add the state suffix
    return city_name.lower() + state_suffix


# In[6]:


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Get the number from the form
        number = request.form.get('number', type=int)
        if number is not None:
            a = list(df[df["zip"] == number]["primary_city"])
            b = "-"+(list(df[df["zip"] == number]["state"]))[0]
            formatted_city_name = format_city_name(a[0], b)
            result = formatted_city_name
    return render_template_string(HTML, result=result)


# In[7]:


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


# In[ ]:




