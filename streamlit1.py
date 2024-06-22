import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('My first App for Streamlit')
st.header('This is header')
st.caption('Caption')
st.markdown('''
            This is __bold__ and this is _italic_ and this is

             `def fn(a, b): 
                return a + b` 

            and this is [link for google](https://www.google.com)''')

st.image('https://th-thumbnailer.cdn-si-edu.com/ii_ZQzqzZgBKT6z9DVNhfPhZe5g=/fit-in/1600x0/filters:focal(1061x707:1062x708)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer_public/55/95/55958815-3a8a-4032-ac7a-ff8c8ec8898a/gettyimages-1067956982.jpg')

st.video('https://www.youtube.com/watch?v=nVbm5nImTj0')


city = st.radio('choose city:', ['lahore', 'karachi', 'islamabad'])

st.markdown(f''' Your selected city is: **{city}** ''')

st.multiselect('choose city:', ['lahore', 'karachi', 'islamabad'])

st.selectbox('choose city:', ['lahore', 'karachi', 'islamabad'])

st.checkbox('I agree')

st.text_input('Enter text')
st.text_area('Enter text')

st.number_input('Enter number', 0, 100)
st.slider('Slide', 0, 100)
st.select_slider('Select', ['bad', 'good', 'excellent'])

st.date_input('Enter date')
st.time_input('Enter time')

st.success('Text')
st.info('Info')
st.warning('Warning')
st.error('Error')


st.markdown("<h1 style='text-align: center; color: blue;'>Hello World</h1>", unsafe_allow_html=True)

st.markdown('''
<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table> ''', unsafe_allow_html=True)
st.write(' \n ')
st.markdown('''
            | Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Cell 2   | Cell 3   |
| Row 2    | Cell 5   | Cell 6   |
| Row 3    | Cell 8   | Cell 9   |
''')

st.sidebar.title('This is sidebar title')
st.sidebar.write('''
                About me 
                 
                Contact 
                 
                Location
                 
                 [Linkedin](https://www.linkedin.com)
                 ''')

st.header('Columns')
c1,c2 = st.columns(2)
with c1:
    st.video('https://www.youtube.com/watch?v=nVbm5nImTj0')
with c2:
    st.image('https://th-thumbnailer.cdn-si-edu.com/ii_ZQzqzZgBKT6z9DVNhfPhZe5g=/fit-in/1600x0/filters:focal(1061x707:1062x708)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer_public/55/95/55958815-3a8a-4032-ac7a-ff8c8ec8898a/gettyimages-1067956982.jpg')

st.header('Tabs')
c1,c2 = st.tabs(['Video', 'Image'])
with c1:
    st.video('https://www.youtube.com/watch?v=nVbm5nImTj0')
with c2:
    st.image('https://th-thumbnailer.cdn-si-edu.com/ii_ZQzqzZgBKT6z9DVNhfPhZe5g=/fit-in/1600x0/filters:focal(1061x707:1062x708)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer_public/55/95/55958815-3a8a-4032-ac7a-ff8c8ec8898a/gettyimages-1067956982.jpg')


df = pd.DataFrame({'Job': ['Data Scientist', 'Data Analyst', 'Data Engineer'], 'Avg Salary': [100000, 80000, 120000]})

st.dataframe(df)
st.table(df)

fig, ax = plt.subplots() 
ax.bar(df['Job'], df['Avg Salary'])
st.pyplot(fig)


st.header('Plotly Charts')
c1,c2 = st.columns(2)
with c1:
    fig1 = px.histogram(df, x='Job', y='Avg Salary', title='Average Salary')
    st.plotly_chart(fig1)
with c2:
    fig2 = px.box(df, x='Job', y='Avg Salary', title='Average Salary')
    st.plotly_chart(fig2)

