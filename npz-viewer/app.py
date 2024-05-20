import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Increase file upload size limit


# Define the plot function using Matplotlib
def plot_image(image: np.ndarray, cmap: str, key: str, channel: int):
    """
    Plot a single channel image.

    Args:
        image (np.ndarray): The image to plot.
        cmap (str): The colormap to use for plotting.
        key (str): The key from the dataset being processed.
        channel (int): The channel number being processed.
    """
    fig, ax = plt.subplots()
    cax = ax.imshow(image, cmap=cmap, origin="lower")
    ax.set_title(f"{key} - Channel {channel}")

    # Ensure the colorbar has the same height as the image
    divider = make_axes_locatable(ax)
    cax_cb = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(cax, cax=cax_cb)

    st.pyplot(fig)


# Streamlit app
st.title("NPZ File Visualizer")

uploaded_file = st.file_uploader("Choose an NPZ file", type="npz")

if uploaded_file is not None:
    data = np.load(uploaded_file)

    cmap = st.selectbox("Select colormap", plt.colormaps())

    for key in data:
        st.write(f"Processing {key}")
        array = data[key]
        for channel in range(array.shape[1]):
            image = array[0, channel, :, :]
            plot_image(image, cmap, key, channel)
