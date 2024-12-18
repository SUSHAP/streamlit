import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from io import BytesIO

# Title of the app
st.title("SMILES to Image Converter")

# App description
st.write(
    "This app takes a **SMILES** string as input and generates the corresponding molecular structure image. "
    "For example, try 'CCO' (Ethanol) or 'C1=CC=CC=C1' (Benzene)."
)

# Input for SMILES string
smiles = st.text_input("Enter SMILES string:")

# Example button
if st.button("Try Example"):
    smiles = "C1=CC=CC=C1"  # Benzene
    st.experimental_set_query_params()

# Validate and process input
if smiles.strip():
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            # Generate molecule image as PIL Image
            img = Draw.MolToImage(mol, size=(300, 300))
            
            # Save the image in memory
            img_buffer = BytesIO()
            img.save(img_buffer, format="PNG")
            img_buffer.seek(0)  # Reset buffer pointer
            
            # Display image in the app
            st.image(img, caption="Generated Molecule Image")
            
            # Add a download button
            st.download_button(
                label="Download Molecule Image as PNG",
                data=img_buffer,
                file_name="molecule.png",
                mime="image/png"
            )
        else:
            st.error("Invalid SMILES string. Please try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.warning("Please enter a valid SMILES string.")
