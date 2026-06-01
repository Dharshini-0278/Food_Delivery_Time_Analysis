
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df):

    plt.figure(figsize=(8,5))

    sns.histplot(df['Delivery_Time_min'], bins=20,color='skyblue',edgecolor='black' )

    plt.title('Distribution of Delivery Time')

    plt.xlabel('Delivery Time (minutes)')

    plt.ylabel('Frequency')


    plt.show()






def plot_scatter(df):

    plt.figure(figsize=(8,5))

    sns.scatterplot(
        x='Distance_km',
        y='Delivery_Time_min',
        data=df
    )

    plt.title('Distance vs Delivery Time')

    plt.show()