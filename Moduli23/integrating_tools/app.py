import streamlit as st
import requests
import pandas as pd

st.title("Project Managment App")

st.header("Add a developer")
dev_name=st.text_input("Developer Name")
dev_experience=st.number_input("Experience(Years)",min_value=0,max_value=50,value=0)

if st.button("Create Developer"):
    dev_data={"name":dev_name,"experience":dev_experience}
    response=requests.post("http://localhost:8000/developers/",json=dev_data)
    st.json(response.json())


st.header("Add a Project")
proj_title=st.text_input("Project Title")
proj_desc=st.text_area("Project Description")
proj_langs=st.text_input('Language Used(Comma-separeted')
lead_Dev_name=st.text_input("Lead Developer Name")
lead_Dev_exp=st.number_input("Lead Develper Experience(years",min_value=0,max_value=50,value=0)

if st.button("Create Project"):
    lead_Dev_data={"name":lead_Dev_name,"experience":lead_Dev_exp}
    proj_Data={
        "title":proj_title,
        "description":proj_desc,
        "languages":proj_langs,
        "lead_developer":lead_Dev_data
    }
    response = requests.post("http:/localhost:8000/projects/",json=proj_Data)
    st.json(response.json)

    st.header('project Dashboard')

if st.button("Get Projects"):
        response= requests.get("http:/localhost:8000/projects/")
        proj_data=response.json(['projects'])

        if proj_Data:
            proj_df=pd.DataFrame(proj_Data)

            st.subheader('Project Overview')
            st.dataframe(proj_df)

            st.subheader("Project Details")
            for project in proj_data:
                st.markdown(f"**Title:**{project['title']}")
                st.markdown(f"**Description:**{project['description']}")
                st.markdown(f"**Language:**{project['language']}")
                st.markdown(f"**Lead Developer:**{project['lead_developer']['name']} with{project['lead_developer']['experience']}years of experience")
                st.markdown(f"---")
        else:
            st.warning("No projects found")
