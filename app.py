"""Created on Thu Jun  1 07:00:53 2023@author: abhishek"""##########import all necessary librariesimport streamlit as stimport plotly.express as pximport pandas as pdimport numpy as npst.title("EDA APP")st.markdown("""This app performs EDA*   **Python Libraries :** Streamlit,Pandas,Plotly ....            """)###########upload the filefile_byte=st.file_uploader("Upload a file",type="csv")#########check if file has been uploaded or notif file_byte is not None:    #reading the file    df=pd.read_csv(file_byte)    st.dataframe(df.head())    obj=[] #empty list for objects datatype    int_float=[]    for i in df.columns:        clas=df[i].dtypes        if clas =='object':           obj.append(i)        else:           int_float.append(i)             ########## Adding submit Button sidebarwith st.form(key='my_form'):    with st.sidebar:        st.sidebar.header("To remove NULL values press the button below")        submit_button=st.form_submit_button(label='Remove NULL')        ############# if we click remove NULL Nulll values will be replaced with mean or mode if submit_button:    for i in df.columns:        clas=df[i].dtypes        if clas =='object':            df[i].fillna(df[i].mode()[0],inplace=True)        else:            df[i].fillna(df[i].mean(),inplace=True)            ######### finding count of null value in each columnlis=[]    for i in df.columns:    n=sum(df[i].isnull())    lis.append(n)       ##########   if no. of null values are 0 it will display some text otherwise it will display barplot by each columnif max(lis)==0:   st.write("Total no. of NULL Value "+str(max(lis)))else:   st.write("Bar Plot to know no. of NULL values in each column")   st.write("Total no. of NULL values "+str(sum(lis)))   fig2=px.bar(x=df.columns,y=lis,labels={'x':"Columns Names",'y':"No. of Null Values"})   st.plotly_chart(fig2)          ####### Frequency Plot for categorical columnsst.sidebar.header("Select Variable")selected_pos=st.sidebar.selectbox('Object Variable',obj)st.write("Bar Plot to know frequency of each category")frequency_data=df[selected_pos].value_counts()fig=px.bar(frequency_data,x=frequency_data.index,y=selected_pos,labels={'x':selected_pos,'y':'count'})st.plotly_chart(fig)########   Histogramst.sidebar.header("Select Variable")selected_pos1=st.sidebar.selectbox('Int or Float Variable',int_float)st.write("Bar Plot to know count of value based on range")counts,bins=np.histogram(df[selected_pos1],bins=range(int(min(df[selected_pos1])),int(max(df[selected_pos1])),int(max(df[selected_pos1])/10)))bins=0.5*(bins[:-1]+bins[1:])fig1=px.bar(x=bins,y=counts,labels={'x':selected_pos1,'y':'count'})st.plotly_chart(fig1)                         ##### Corelation Chartst.sidebar.header("Select Variable")selected_pos2=st.sidebar.multiselect('Int or float Variable Correlation',int_float)st.write("Scatter Plot for corealtion")if len(selected_pos2)==2:   fig3=px.scatter(df,x=selected_pos2[0],y=selected_pos2[1])   st.plotly_chart(fig3)else:   st.write("Select Two Variables")                                                        