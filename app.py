import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Replace with your PostgreSQL database connection URI
DATABASE_URI = 'postgresql://data_puppy_user:z54o9ZMvBRHaxqbK9kfXqd9KIwZVREja@dpg-cm1uq8fqd2ns73d6ed8g-a.oregon-postgres.render.com/data_puppy'
# Create a database engine
engine = create_engine(DATABASE_URI)

# Function to fetch data from the database
def fetch_data():
    query = 'SELECT * FROM your_table'
    df = pd.read_sql(query, engine)
    return df

# Main Streamlit app
def main():
    st.title('Puppies Database Viewer')

    # Fetch data from the database
    data = fetch_data()

    # Display the data in a table
    st.dataframe(data, hide_index=True)

if __name__ == '__main__':
    main()



#filled_space =  df['Status'].values.sum()
#empty_space = len(df) -  filled_space

#st.header("Occupency Table")
#st.dataframe(df)

#st.text(f"Occuped space {filled_space}.")
#st.text(f"Available space {empty_space}.")
