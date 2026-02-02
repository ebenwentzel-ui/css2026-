# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 15:45:55 2026
@author: ebenw
"""

import streamlit as st
import os

# -----------------------------
# PAGE CONFIG (must be first Streamlit call)
# -----------------------------
st.set_page_config(
    page_title="Eben Wentzel | Computational Biology",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# PATHS (GitHub-safe)
# Anchors everything to this script's folder, not CWD.
# -----------------------------
APP_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(APP_DIR, "assets")

# -----------------------------
# ASSET FILENAMES (edit these if you rename files)
# -----------------------------
BANNER_FILE = "0d10d58a-81f0-451a-8c83-da4389379dc1.png"
ABOUT_IMAGE_FILE = "00418346-55f5-496c-b4e4-04b724f2ace3.png"
DOCKING_IMAGE_FILE = "Docking.jpg"

banner_path = os.path.join(ASSETS_DIR, BANNER_FILE)
about_img_path = os.path.join(ASSETS_DIR, ABOUT_IMAGE_FILE)
docking_img_path = os.path.join(ASSETS_DIR, DOCKING_IMAGE_FILE)

# -----------------------------
# GLOBAL CSS: background + top spacing + stop horizontal scroll
# -----------------------------
st.markdown(
    """
    <style>
      .stApp { background: #d9f0ff; }

      /* Remove extra space above the first element */
      .block-container { padding-top: 0rem; }

      html, body { overflow-x: hidden; }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# FULL-WIDTH BANNER: remove side padding BEFORE rendering banner
# -----------------------------
st.markdown(
    """
    <style>
      .block-container {
        padding-left: 0rem !important;
        padding-right: 0rem !important;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# Optional debug (collapsed)
with st.expander("Debug (paths)", expanded=False):
    st.write("APP_DIR:", APP_DIR)
    st.write("ASSETS_DIR exists:", os.path.isdir(ASSETS_DIR))
    st.write("ASSETS_DIR contents:", os.listdir(ASSETS_DIR) if os.path.isdir(ASSETS_DIR) else "NO assets folder")
    st.write("Banner exists:", os.path.exists(banner_path))
    st.write("About image exists:", os.path.exists(about_img_path))
    st.write("Docking image exists:", os.path.exists(docking_img_path))

# Banner at top
with st.container():
    if os.path.exists(banner_path):
        st.image(banner_path, use_container_width=True)
    else:
        st.error(f"Banner not found. Expected: {banner_path}")

# -----------------------------
# Restore normal padding for the rest of the page
# -----------------------------
st.markdown(
    """
    <style>
      .block-container {
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        padding-top: 2rem !important;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# ABOUT ME
# -----------------------------
with st.container():
    st.header("About Me")

    col_text, col_img = st.columns([2, 1], gap="large")

    with col_text:
        st.write(
            "My work sits at the intersection of pharmacology, computation, and experimental biology, "
            "with a central focus on using in silico approaches to interrogate complex drug–biological "
            "systems before they are explored experimentally. I am motivated by mechanistic understanding "
            "rather than surface-level outcomes. I want to know not only whether a drug works, but how it works, "
            "why it fails, and under which assumptions any conclusion remains valid. This emphasis on first principles "
            "shapes how I think about research problems and how I design studies."
        )
        st.write(
            "I am particularly drawn to in silico research because it enforces intellectual rigor. Computational models "
            "demand explicit assumptions, formal parameterisation, and quantitative justification. There is little room "
            "for hand-waving. Either a model converges or it does not; either a hypothesis survives stress-testing or it collapses. "
            "I find this constraint productive rather than limiting. It strips away narrative comfort and forces clarity, which is "
            "essential when dealing with biological systems that are inherently complex and noisy."
        )
        st.write(
            "My interest in drugs arises from their role as controlled perturbations of biological systems. A drug is a physical entity "
            "governed by chemistry and physics, yet its effects propagate through multiple biological scales, from molecular interactions "
            "to cellular and phenotypic outcomes. Understanding this translation requires tools that can move seamlessly between abstraction "
            "and experiment. Computation provides that bridge, allowing hypotheses to be refined and constrained before they encounter the "
            "variability of the laboratory."
        )
        st.write(
            "Broadly, my research interests include structure–function relationships in drug–target interactions, cytoskeletal dynamics and their "
            "pharmacological modulation, and mechanism-driven drug repositioning strategies. I am particularly interested in integrating in silico "
            "predictions with in vitro validation in a tightly coupled feedback loop. I am most engaged by problems that are complex, multivariate, "
            "and resistant to simple explanations."
        )
        st.write(
            "A core aspect of my interest in computational research is its reliance on physics and mathematics. Molecular dynamics, energy landscapes, "
            "statistical mechanics, and stochastic modelling are not auxiliary tools but foundational components of meaningful in silico work."
        )
        st.write(
            "Looking ahead, I see in silico research moving beyond a supportive role toward becoming a primary driver of hypothesis generation in drug development: "
            "mechanistically informed simulations that meaningfully constrain experimental design, prioritising interpretability and uncertainty quantification."
        )
        st.write(
            "My approach to research is inherently iterative. I formalise assumptions computationally, generate constrained and testable hypotheses, interrogate them "
            "experimentally, and refine the models based on failure rather than confirmation."
        )

    with col_img:
        if os.path.exists(about_img_path):
            st.image(
                about_img_path,
                caption="Computational biology mindset",
                use_container_width=True
            )
        else:
            st.warning(f"About image not found: {about_img_path}")

# -----------------------------
# RESEARCH THEMES
# -----------------------------
with st.container():
    st.header("Research Themes")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("In silico work")
        st.write("My primary objective in the in silico component is to characterise epothilone–target interactions at a mechanistic level and generate testable hypotheses that meaningfully guide wet-lab work. This includes:")
        st.write("• Defining binding modes, stability, and interaction networks using molecular docking and molecular dynamics simulations.")
        st.write("• Probing how structural variations influence microtubule binding, conformational dynamics, and potential resistance-relevant interactions.")
        st.write("• Identifying non-obvious structure–function relationships that are not apparent from static models or literature consensus.")
        st.write("• Reducing experimental ambiguity by narrowing the hypothesis space before in vitro validation.")
        st.write("The goal is not to produce “pretty simulations,” but to constrain reality to make the experimental phase sharper, cheaper, and more informative.")

    with col2:
        st.subheader("In vitro work")
        st.write("The in vitro component exists to interrogate and falsify the computational predictions. My objectives here are to:")
        st.write("• Validate predicted drug effects on cytoskeletal dynamics, cell viability, and relevant phenotypic readouts.")
        st.write("• Quantify dose–response relationships informed by in silico predictions rather than exploratory guessing.")
        st.write("• Examine discrepancies between computational models and biological outcomes to refine both.")
        st.write("• Build a coherent mechanistic narrative that links molecular interaction → cellular effect → therapeutic relevance.")
        st.write("The lab is not a fishing expedition. It is a controlled test of ideas already shaped by computation.")

# -----------------------------
# CONTACT + FINAL IMAGE (fixed: no invalid 'with col_img' reuse)
# -----------------------------
with st.container():
    st.header("Contact")
    st.markdown(
        "Email: ebens.research@gmail.com  \n"
        "LinkedIn: https://za.linkedin.com/in/eben-wentzel-4013352a4"
    )

if os.path.exists(docking_img_path):
    st.image(
        docking_img_path,
        caption="The final product",
        width=400
    )


