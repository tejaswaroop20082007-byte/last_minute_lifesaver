import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Last-Minute Life Saver", page_icon="🚀", layout="centered")

st.title("🚀 Last-Minute Life Saver MVP")
st.markdown("### *Your AI-Powered Autonomous Accountability Partner*")
st.write("---")


try:
    # Safely reading from Streamlit's local or cloud secrets manager
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    st.error("🔒 Security Alert: Configuration key missing or invalid. Please check your local secrets file.")


user_task = st.text_input(
    "🎯 What critical academic task, topic, or exam are you currently panicking about?",
    placeholder="e.g., Studying for Java OOP Lab Exam covering Inheritance and Interfaces"
)

tab1, tab2 = st.tabs(["🧠 Agentic Task Deconstructor", "🔥 Context-Aware Roaster"])


with tab1:
    st.markdown("#### 🛰️ Multi-Agent Planning & Risk Optimization Pipeline")
    st.write("Watch our autonomous planning loop analyze, deconstruct, and stress-test your task requirements in real-time.")
    
    if st.button("🚀 Activate Deconstruction Pipeline", key="feat1_btn"):
        if not user_task.strip():
            st.error("Please provide a task or topic first!")
        else:
            # Open an interactive status block to visibly show the agent hand-off to the judges
            with st.status("🧠 Initiating Multi-Agent Workflow...", expanded=True) as status:
                
                status.write("🛰️ Dispatching Blueprint Agent: Deconstructing objective into architectural milestones...")
                
                blueprint_prompt = f"""
                You are a technical Project Blueprint Agent. 
                Deconstruct the following high-level student objective into a clear, chronological list of technical milestones or study phases:
                Objective: "{user_task}"
                
                Output ONLY a clean, numbered list of steps. Do not add introductory or concluding prose.
                """
                
                blueprint_response = model.generate_content(blueprint_prompt)
                raw_plan = blueprint_response.text
                
                status.write("🔍 Dispatching Execution Critic Agent: Analyzing sequential risks and calculating time buffers...")
                
                critic_prompt = f"""
                You are an Execution Optimizer Agent. Review the following raw project/study plan:
                {raw_plan}
               
                
                Your job is to optimize this plan for an engineering student under extreme time constraints. Rewrite the plan by:
                1. Assigning strict, aggressive, but realistic time allocations to each step.
                2. Autonomously identifying exactly ONE critical technical risk, bottleneck, or "Single Point of Failure" for each step (e.g., runtime exceptions, environment path mismatches, forgotten import statements).
                3. Formatting the output beautifully with clear markdown emojis.
                """
                
                # Handing off data: The output of Agent 1 is directly interpolated into Agent 2's prompt environment
                critic_response = model.generate_content(critic_prompt)
                final_optimized_plan = critic_response.text
                
                # Close out the status box cleanly
                status.update(label="🏁 Strategic Execution Roadmap Finalized!", state="complete", expanded=False)
            
            # Display final results proudly
            st.success("Analysis Complete!")
            st.subheader("📋 Your Optimized Agentic Roadmap")
            st.markdown(final_optimized_plan)

with tab2:
    st.markdown("#### 🔥 Deep Contextual Accountability Trigger Generator")
    st.write("Generate personalized motivational triggers strictly customized to the syntax and concepts of your task topic.")
    
    if st.button("🔥 Generate Behavioral Triggers", key="feat2_btn"):
        if not user_task.strip():
            st.error("Please provide a task or topic first!")
        else:
            with st.spinner("Analyzing profile context and parsing domain concepts..."):
                roast_prompt = f"""
                You are a witty, unhinged, but deeply supportive academic accountability coach. 
                Analyze this specific topic/task the student is procrastinating on: "{user_task}"
                
                Generate exactly 4 distinct, highly creative options or slogans designed to force them to stop slacking.
                CRITICAL: You must use advanced inner-domain jokes, puns, terms, or conceptual metaphors related explicitly to the provided topic (e.g., if it's Java, use 'NullPointerException', 'garbage collection', 'compilation errors', 'abstract classes'). 
                 Make it sharply witty but deeply motivating for an engineering undergraduate.
                """
                
                roast_response = model.generate_content(roast_prompt)
                
            st.subheader("💀 Your Custom Accountability Triggers")
            st.markdown(roast_response.text)