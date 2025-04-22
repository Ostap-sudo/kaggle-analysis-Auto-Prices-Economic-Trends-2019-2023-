import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine


db_user = 'postgres'
db_password = 'ostap112'
db_host = 'localhost'
db_port = '5432'
db_name = 'car_prices'

# 🔌 Підключення до бази
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# 📥 Завантаження таблиці car_data у DataFrame
query = 'SELECT * FROM car_data;'
df = pd.read_sql(query, engine)

# 📅 Перетворення колонки дати
df['month_year'] = pd.to_datetime(df['month_year'])
print(df.columns)


# 📈 Побудова графіку: Units Sold з часом
plt.figure(figsize=(12, 6))
sns.lineplot(x='month_year', y='units_sold', data=df, marker='o')
plt.title('Units Sold Over Time')
plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()
plt.show()

# 📈 Динаміка цін: New Price vs Used Price
plt.figure(figsize=(12, 6))
sns.lineplot(x='month_year', y='new_price', data=df, label='New Price', marker='o')
sns.lineplot(x='month_year', y='used_price', data=df, label='Used Price', marker='x')
plt.title('Price Dynamics: New vs Used')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
# 📉 Вплив інфляції на продажі
plt.figure(figsize=(12, 6))
sns.scatterplot(x='inflation_rate', y='units_sold', data=df)
plt.title('Impact of Inflation on Units Sold')
plt.xlabel('Inflation Rate (%)')
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()
plt.show()



