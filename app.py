import streamlit as st
import google.generativeai as genai
# Note: google.colab is not needed in a Streamlit app deployed on Streamlit Cloud

# Configure the Google Generative AI client
try:
    # Accessing secrets in Streamlit Cloud
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    if not GOOGLE_API_KEY:
         st.error("Google API Key not found. Please set GOOGLE_API_KEY in Streamlit Secrets.")
         ai_model = None
    else:
        genai.configure(api_key=GOOGLE_API_KEY)
        # Initialize the Generative Model
        ai_model = genai.GenerativeModel('gemini-1.5-flash-latest')
        st.success("Google Generative AI model initialized successfully.")
except Exception as e:
    st.error(f"Error initializing Google Generative AI model: {e}")
    st.warning("Please ensure your GOOGLE_API_KEY is set correctly in Streamlit Secrets.")
    ai_model = None # Set ai_model to None if initialization fails

# Define get_ai_response
def get_ai_response(prompt):
    """Sends a prompt to the AI model and returns the response."""
    if ai_model is None:
        st.error("AI model not initialized. Cannot get response.")
        return "AI model not available."
    try:
        response = ai_model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error getting AI response: {e}")
        return f"Error getting AI response: {e}"

# Define analyze_feedback
def analyze_feedback(transcribed_text, image_info="No specific image information provided."):
    """
    Analyzes the transcribed feedback and image information using the AI model.
    """
    if not transcribed_text:
        return "No transcribed text to analyze."

    prompt = f"""
    You are an AI assistant specializing in architectural feedback analysis.
    You have received the following feedback from an instructor regarding a student's architectural work:

    "{transcribed_text}"

    The feedback is related to an architectural work described as:
    "{image_info}"

    Please analyze this feedback in the context of architectural principles.
    Identify key points, areas for improvement, and potential strengths mentioned in the feedback.
    Provide a concise summary of the analysis.
    """
    return get_ai_response(prompt)

# Define generate_case_studies
def generate_case_studies(ai_analysis_text):
    """
    Generates case studies based on the AI analysis.
    """
    if not ai_analysis_text or "AI model not available." in ai_analysis_text:
        return "Cannot generate case studies without a valid AI analysis."

    prompt = f"""
    Based on the following architectural feedback analysis:
    "{ai_analysis_text}"

    Generate relevant illustrated case studies that exemplify the concepts discussed.
    Focus on real-world examples or well-known architectural projects.
    Provide brief explanations for each case study highlighting its relevance to the feedback analysis.
    """
    return get_ai_response(prompt)

# Define generate_critical_thinking_prompts
def generate_critical_thinking_prompts(ai_analysis_text):
    """
    Generates critical thinking prompts based on the AI analysis.
    """
    if not ai_analysis_text or "AI model not available." in ai_analysis_text:
        return "Cannot generate critical thinking prompts without a valid AI analysis."

    prompt = f"""
    Based on the following architectural feedback analysis:
    "{ai_analysis_text}"

    Generate critical thinking prompts and brainstorming questions that can help a student deepen their understanding and explore alternative design solutions related to the feedback.
    """
    return get_ai_response(prompt)

# Define interpret_abstract_concepts
def interpret_abstract_concepts(ai_analysis_text):
    """
    Interprets abstract concepts mentioned in the AI analysis.
    """
    if not ai_analysis_text or "AI model not available." in ai_analysis_text:
        return "Cannot interpret abstract concepts without a valid AI analysis."

    prompt = f"""
    Based on the following architectural feedback analysis:
    "{ai_analysis_text}"

    Identify any abstract or complex architectural concepts mentioned or implied, and provide clear, simple interpretations and explanations to aid student understanding and decision-making.
    """
    return get_ai_response(prompt)

# Streamlit App Layout
st.set_page_config(layout="wide", page_title="Architectural Feedback Analyzer")

st.title("📐 Architectural Feedback Analyzer")

st.markdown("""
This application helps students analyze architectural feedback using AI.
Enter your text feedback below, and the AI will provide a detailed analysis,
relevant case studies, critical thinking prompts, and interpretations of abstract concepts.
""")

st.header("📝 Enter Your Architectural Feedback")
user_feedback_text = st.text_area("Paste your feedback here:", height=200, key="feedback_input")

# Use a state variable to store analysis result and trigger subsequent generations
if 'analysis_result' not in st.session_state:
    st.session_state['analysis_result'] = None

if st.button("✨ Analyze Feedback"):
    if user_feedback_text:
        st.header("🤖 AI Analysis and Insights")
        with st.spinner("Analyzing feedback..."):
            analysis_text = analyze_feedback(user_feedback_text)
            st.session_state['analysis_result'] = analysis_text # Store result in session state

# Display analysis and generate subsequent outputs if analysis is available
if st.session_state['analysis_result']:
    analysis_text = st.session_state['analysis_result']
    st.subheader("📊 AI Analysis Result:")
    st.markdown(analysis_text) # Use markdown to render the analysis

    if "AI model not available." not in analysis_text and "Error getting AI response" not in analysis_text:
        st.markdown("---") # Separator

        st.subheader("🏛️ Illustrated Case Studies")
        with st.spinner("Generating case studies..."):
            case_studies_output = generate_case_studies(analysis_text)
        st.markdown(case_studies_output) # Use markdown

        st.markdown("---") # Separator

        st.subheader("🤔 Critical Thinking Prompts")
        with st.spinner("Generating prompts..."):
            critical_thinking_output = generate_critical_thinking_prompts(analysis_text)
        st.markdown(critical_thinking_output) # Use markdown

        st.markdown("---") # Separator

        st.subheader("🧠 Interpretations of Abstract Concepts")
        with st.spinner("Interpreting concepts..."):
            interpretations_output = interpret_abstract_concepts(analysis_text)
        st.markdown(interpretations_output) # Use markdown
    else:
        st.error("Analysis failed, cannot generate further outputs.")


st.markdown("---") # Separator
st.markdown("Built with Streamlit and Google Generative AI.")
