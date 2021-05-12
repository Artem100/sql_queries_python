from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres2:newpass@10.0.6.90:5432/new_1', echo=False)

# Get data from db use query
result = engine.execute("SELECT * FROM student")
row = result.fetchall()
print(row)
# result.close()

# Add new city
user_1 = engine.execute("INSERT INTO test_data (city, population) VALUES ('aLALA4', 70) ")
user_1_result = engine.execute("SELECT * FROM test_data WHERE city='aLALA4' and population=70")
row_2 = user_1_result.fetchall()
print(row_2)
negth = len(row_2)
print("lllllllllll: ",negth)
user_1_result.close()

# Delete all data in table
user_delete = engine.execute("truncate table test_data")
user_delete.close()

# Check that city was deleted
user_2_result = engine.execute("SELECT * FROM test_data WHERE city='aLALA4' and population=70")
row_3 = user_2_result.fetchall()
negth = len(row_3)
print(negth)