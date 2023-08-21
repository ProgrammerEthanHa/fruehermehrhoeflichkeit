import streamlit as st
import pandas as pd
import altair as alt

st.header("Früher mehr Höflichkeit")
st.subheader("Sind Sie der Meinung, dass Menschen heute höflicher oder weniger höflich sind als früher?")

source = pd.DataFrame({
        'Anteil(%)': [75, 16, 4],
        'Meinung': ['Die Menschen waren früher höflicher als heute', 'Die Menschen waren früher genauso höflich wie heute', 'Die Menschen sind heute höflicher als früher']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Meinung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    2015
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: YouGov")