from scipy.stats import f_oneway

def traffic_anova(low, medium, high):

    f_stat, p_value = f_oneway(low, medium, high)

    return f_stat, p_value
