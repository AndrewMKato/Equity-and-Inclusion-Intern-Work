import matplotlib.pyplot as plt

# Due to apparent issues between the set-up of the CSV and how pd forms Dataframes, the values are hardcoded for now.
plt.style.use('ggplot')

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

dom_am_indian_percentage = [0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4]
dom_black_percentage = [7.9, 7.9, 7.9, 7.9, 7.7, 7.7, 7.6, 7.5, 7.4, 7.1]
dom_hispanic_percentage = [15.9, 16.6, 17.2, 18.0, 18.6, 19.5, 20.2, 20.8, 21.4, 21.5]
dom_two_or_more_percentage = [0.3, 0.4, 0.6, 0.7, 0.8, 0.9, 1.0, 1.3, 1.3, 1.6]
dom_unknown_percentage = [3.1, 2.6, 2.5, 2.3, 2.5, 2.7, 3.0, 3.5, 3.4, 3.2]
dom_asian_and_native_hawaii_percentage = [18.0, 18.4, 18.7, 19.1, 19.5, 19.9, 20.1, 20.3, 20.2, 19.9]
dom_white_percentage = [42.2, 41.7, 41.1, 40.2, 39.2, 37.8, 36.5, 35.0, 33.6, 31.5]

inter_am_indian_percentage = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
inter_black_percentage = [0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.5, 0.5, 0.6, 0.6]
inter_hispanic_percentage = [3.6, 3.6, 3.7, 3.6, 3.5, 3.6, 3.5, 3.6, 4.0, 4.1]
inter_two_or_more_percentage = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1]
inter_unknown_percentage = [0.5, 0.4, 0.3, 0.3, 0.3, 0.4, 0.4, 0.5, 0.6, 3.1]
inter_asian_and_native_hawaii_percentage = [5.5, 5.4, 5.2, 5.1, 5.0, 4.9, 5.0, 4.9, 5.0, 5.1]
inter_white_percentage = [2.0, 2.0, 1.8, 1.8, 1.8, 1.7, 1.7, 1.7, 2.0, 1.9]

am_indian_percentage = [i + j for i, j in zip(dom_am_indian_percentage, inter_am_indian_percentage)]
black_percentage = [i + j for i, j in zip(dom_black_percentage, inter_black_percentage)]
hispanic_percentage = [i + j for i, j in zip(dom_hispanic_percentage, inter_hispanic_percentage)]
two_or_more_percentage = [i + j for i, j in zip(dom_two_or_more_percentage, inter_two_or_more_percentage)]
unknown_percentage = [i + j for i, j in zip(dom_asian_and_native_hawaii_percentage, inter_unknown_percentage)]
asian_and_native_hawaii_percentage = [i + j for i, j in zip(dom_unknown_percentage, inter_asian_and_native_hawaii_percentage)]
white_percentage = [i + j for i, j in zip(dom_white_percentage, inter_white_percentage)]

print(am_indian_percentage)

names = ('American Indian', 
    'Black',
    'Hispanic',
    'Two or More Races',
    'Unknown',
    'Asian and Native Hawaiian',
    'White'
    )

plt.stackplot(years, 
    am_indian_percentage, 
    black_percentage,
    hispanic_percentage,
    two_or_more_percentage,
    unknown_percentage,
    asian_and_native_hawaii_percentage,
    white_percentage,
    labels=names)

plt.legend()

plt.locator_params(axis='x', integer=True, tight=True)

plt.xlabel('Year')
plt.ylabel('Proportion (in percent)')

plt.title('''Racial/Ethnic Diversity of Non-Student Staff, 
Universitywide, October 2011 to 2020''')

plt.tight_layout()

plt.savefig('model.png')
plt.show()