import streamlit as st
import teamtopology as tt
import fineflowevaluation as fine

def main():
    st.title("BU Team Flow Analysis")

    # Input dictionary using Streamlit components
    st.header("Input Team Flow Dictionary")
    BU_TeamFlow = st.text_area("Enter the dictionary in JSON format", value='{"Delivery Team 1": ["Cloud Team", "Compliance", "Security"], "Delivery Team 2": ["SRE","Compliance"], "Delivery Team 3": ["Compliance"], "Cloud Team": ["Network", "DBTeam","Security"], "Network": ["WinTel DNS", "Security"], "Security": [], "DbTeam": ["Security"], "SRE": [], "WinTel DNS": [], "Compliance": []}')
    BU_TeamFlow = eval(BU_TeamFlow)  # Evaluate the input string as a dictionary

    # Find topology
    st.header("Topology")
    ttopology = tt.findTopology(BU_TeamFlow)
    st.write(ttopology.items())

    # Evaluate interactions
    st.header("Team Flow Evaluation")
    BU_TeamFlowWithInteractions = st.text_area("Enter the dictionary with interactions in JSON format", value='{"Delivery Team 1": [("Cloud Team","X"), ("Compliance","E"), ("Security","E")], "Delivery Team 2": [("SRE","X"), ("Compliance","E")], "Delivery Team 3": [("Compliance","E")], "Cloud Team": [("Network","C"), ("DBTeam","E"),("Security","E")], "Network": [("WinTel DNS","E"), ("Security", "E")], "Security": [], "DbTeam": [("Security","E")], "SRE": [], "WinTel DNS": [], "Compliance": []}')
    BU_TeamFlowWithInteractions = eval(BU_TeamFlowWithInteractions)  # Evaluate the input string as a dictionary

    ttopology2 = fine.evaluate(BU_TeamFlowWithInteractions, flow=True, imp=True, need=True, energy=True, resilience=True)

    # Output results
    st.header("Evaluation Results")
    for key, value in ttopology2.items():
        st.subheader(f"Key: {key}")
        st.write(value)

if __name__ == "__main__":
    main()
