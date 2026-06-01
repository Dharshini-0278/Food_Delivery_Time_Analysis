def statistical_summary(df):

    return df['Delivery_Time_min'].describe()


def calculate_skewness(df):

    return df['Delivery_Time_min'].skew()