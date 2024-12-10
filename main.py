import streamlit as st
import pandas as pd

def generate_line_chart(csv_path: str, title: str, desc: str, x_label: str, y_label: str) -> None:
    df = pd.read_csv(csv_path)
    reshaped_df = df.pivot(index="num_vectors", columns="k", values="mean_time_secs")
    reshaped_df.columns = [f"k={col}" for col in reshaped_df.columns]
    st.markdown(f'''
        ### {title}
        {desc}
    ''')
    st.line_chart(
        data=reshaped_df,
        x_label=x_label,
        y_label=y_label,
    )

if __name__ == '__main__':
    st.set_page_config(layout="wide") 
    st.markdown('''
    # EigenDB Performance Metrics
    The data has been gathered using a [simple script](https://github.com/Eigen-DB/eigen-db/blob/main/benchmarks/benchmarks.py) for benchmarking EigenDB.            
    ''')

    col1, col2 = st.columns(2)
    with col1:
        generate_line_chart(
            csv_path='./data/indexing_mean.csv', 
            title='Mean indexing time',
            desc='This is the average time to perform similarity search with varying numbers of embeddings and values of k.',
            x_label='Number of embeddings', 
            y_label='Mean time (secs)'
        )
    with col2:        
        generate_line_chart(
            csv_path='./data/indexing_mean.csv',  
            title='Mean embedding insertion time',
            desc='This is the average time to insert an embedding with varying numbers of embeddings and values of k.',
            x_label='Number of embeddings', 
            y_label='Mean time (secs)'
        )
    