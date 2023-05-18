import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA nucleotide web App

This app counts the nucleotide composition of query DNA!

***
""")
st.header('Enter sequence input')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write("""

    ***
""")

st.header("INPUT(DNA Query)")

st.text_area("DNA Query", sequence, height=200)

st.header("OUTPUT(DNA Nucleotide Count)")
st.subheader("1. Print the Dictionary")


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('C', seq.count('C')),
        ('G', seq.count('G')),
        ('T', seq.count('T')),
    ])
    return d


X = DNA_nucleotide_count(sequence)

X

st.subheader("2. Print Text")
st.write('There are  ' + str(X['A']) + '  Adenine')
st.write('There are  ' + str(X['C']) + '  Cytisine')
st.write('There are ' + str(X['G']) + '  Guanine')
st.write('There are ' + str(X['T']) + '  Thymine')


st.subheader('3. Display Data Frame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')

p = alt.Chart(df).mark_bar().encode(
    y='nucleotide',
    x='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)
