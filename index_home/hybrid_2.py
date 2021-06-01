# importing libraries
# import pandas as pd  # high-level data manipulation tool
# import numpy as np  # provides a high-performance multidimensional array object, and tools for working with these arrays
# from .models import Recipe, Heart, Statistics, Ingredients, checked_insert, Unit, UnitRatio, Tags, Post, \
#     ReceIngres, Step, recipe_skill, recipe_tool, TempRecipes, TempHearts, No_Featured, Concat_Recipe_info, No_Recipe
# import re
# from gensim.parsing.preprocessing import remove_stopwords
# from django.db.models import Q
# from functools import reduce
# from collections import Counter


# def clean_keyword(keys):
#     result = (remove_stopwords(re.sub('[^A-Za-z0-9 ]+', '', str(keys)))).split(' ')
#     mylist = list(dict.fromkeys(result))
#     return mylist


# def isKeyExist2(clean_keyword):
#     result_list = []
#     df_hearts = pd.DataFrame(Concat_Recipe_info.objects.all().values())
#     # for i in df_hearts['mas_info']:
#     #     binarySearch(i, clean_keyword[0])   No_Recipe.objects.first().No_of_Recipes
#     lenght = 654
#     print_result = []
#     for i in range(lenght):
#         for ii in clean_keyword:
#             try:
#                 result = binarySearch(df_hearts['mass_info'][i], ii)
#             except:
#                 result = -1
#             if result == -1:
#                 output = "Element not present"
#                 print_result.append("["+str(ii)+"]Element not at: "+str(df_hearts['id'][i]))
#                 break
#             elif result >= 0:
#                 # output = "Element found at index " + str(df_hearts['id'][i])
#                 result_list.append(df_hearts['id'][i])
#                 print_result.append("[" + str(ii) + "]Element at: " + str(df_hearts['id'][i]))
#                 break
#     return [result_list, print_result]


# def binarySearch(arr, x):
#     l = 0
#     r = len(arr)
#     while l <= r:
#         m = l + ((r - l) // 2)
#         res = (x == arr[m])
#         # Check if x is present at mid
#         if res == 0:
#             return m - 1
#             # result.append(str(m - 1))
#         # If x greater, ignore left half
#         if res > 0:
#             l = m + 1
#         # If x is smaller, ignore right half
#         else:
#             r = m - 1
#     return -1


# def collected_keys(isKeyExist2):
#     mylist = dict(Counter(isKeyExist2))
#     # Sort by value
#     mylist = sorted(mylist.values())
#     # remove duplicates
#     # mylist = list(dict.fromkeys(isKeyExist2))
#     return mylist


# def isKeyExist(keys):
#     # using filter() to
#     # perform removal
#     new_keys = str(keys).replace(" ", ",").split(",")
#     test_list = list(filter(None, new_keys))
#     df_hearts = pd.DataFrame(No_Featured.objects.all().values())
#     list_recipe_filter, list_ids_temp = [], []
#     for i in test_list:
#         for ii in range(len(df_hearts)):
#             try:
#                 sam = str(df_hearts['name'][ii] + df_hearts['ingredients'][ii] +
#                           df_hearts['description'][ii]).lower()
#                 if i.lower() in sam:
#                     list_recipe_filter.append(df_hearts['name'][ii])
#                     list_ids_temp.append(df_hearts['id'][ii])
#             except:
#                 print("", end='')
#
#     list_recipe_filter = list(dict.fromkeys(list_recipe_filter))
#     my_dict = {i: list_ids_temp.count(i) for i in list_ids_temp}
#     my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
#     my_dict = list(my_dict.keys())
#     list_ids_temp = list(dict.fromkeys(my_dict))
#     remarks = ""
#     if len(list_ids_temp) < 1:
#         remarks = "No related recipe found. Try our popular recipes instead!"
#         return [remarks, featured_recipes()]
#     else:
#         remarks = "Result to " + keys
#         return [remarks, hybrid(keys)]


# def featured_recipes():
#     df_hearts = pd.DataFrame(No_Featured.objects.all().values())
#
#     # computing the vote mean
#     C = df_hearts['total_hearts'].mean()
#
#     # computing the vote count using 90% quantile
#     m = df_hearts['total_hearts'].quantile(0.9)
#
#     # filtering qualified movies based on 90% quantile
#     qualified_movies = df_hearts.copy().loc[df_hearts['total_hearts'] >= m]
#
#     # defining a function weighted rating
#     def weighted_rating(x, m=m, C=C):
#         v = x['total_hearts']
#         R = x['total_hearts']
#         # Calculation based on the IMDB formula
#         return (v / (v + m) * R) + (m / (m + v) * C)
#
#     # Define a new feature 'score' and calculate its value with `weighted_rating()`
#     qualified_movies['score'] = qualified_movies.apply(weighted_rating, axis=1)
#
#     # Sort movies based on score calculated above
#     qualified_movies = qualified_movies.sort_values('score', ascending=False)
#
#     # Print the top 20 movies
#     return qualified_movies[:20]


# def hybrid(keys):
#     # using filter() to
#     # perform removal
#     new_keys = str(keys).replace(" ", ",").split(",")
#     test_list = list(filter(None, new_keys))
#
#     df_recipes = pd.DataFrame(TempRecipes.objects.all().values())
#     df_hearts = pd.DataFrame(TempHearts.objects.all().values())
#     df_hearts1 = pd.DataFrame(Concat_Recipe_info.objects.all().values())
#
#     # joining two dataset using the 'id' columns
#     # df_hearts = df_hearts.merge(df_recipes, on='id')
#
#     # ['id', 'total_hearts', 'name', 'ingredients', 'description']
#     list_recipe_filter, list_ids_temp = [], []
#     for i in test_list:
#         for ii in range(len(df_hearts)):
#             try:
#                 sam = str(df_hearts1['mass_info'][ii]).lower()
#                 if i.lower() in sam:
#                     list_recipe_filter.append(df_recipes['name'][ii])
#                     list_ids_temp.append(df_hearts['id'][ii])
#             except:
#                 continue
#
#     list_recipe_filter = list(dict.fromkeys(list_recipe_filter))
#     my_dict = {i: list_ids_temp.count(i) for i in list_ids_temp}
#     my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
#     my_dict = list(my_dict.keys())
#     list_ids_temp = list(dict.fromkeys(my_dict))
#
#     # computing the vote mean
#     C = df_hearts['total_hearts'].mean()
#
#     # computing the vote count using 90% quantile
#     m = df_hearts['total_hearts'].quantile(0.9)
#
#     # filtering qualified movies based on 90% quantile
#     qualified_movies = df_hearts.copy().loc[df_hearts['total_hearts'] >= m]
#
#     # defining a function weighted rating
#     def weighted_rating(x, m=m, C=C):
#         v = x['total_hearts']
#         R = x['total_hearts']
#         # Calculation based on the IMDB formula
#         return (v / (v + m) * R) + (m / (m + v) * C)
#
#     # Define a new feature 'score' and calculate its value with `weighted_rating()`
#     qualified_movies['score'] = qualified_movies.apply(weighted_rating, axis=1)
#
#     # Sort movies based on score calculated above
#     qualified_movies = qualified_movies.sort_values('score', ascending=False)
#
#     # Print the top 10 movies
#
#     # Import TfIdfVectorizer from scikit-learn
#     from sklearn.feature_extraction.text import TfidfVectorizer
#
#     # Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
#     tfidf = TfidfVectorizer(stop_words='english')
#
#     # Replace NaN with an empty string
#     df_recipes['description'] = df_recipes['description'].fillna('')
#
#     # Construct the required TF-IDF matrix by fitting and transforming the data
#     tfidf_matrix = tfidf.fit_transform(df_recipes['description'])
#
#     # Output the shape of tfidf_matrix
#
#     # Import linear_kernel
#     from sklearn.metrics.pairwise import linear_kernel
#
#     # Compute the cosine similarity matrix
#     cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
#
#     # Construct a reverse map of indices and movie titles
#     indices = pd.Series(df_hearts.index, index=df_recipes['name']).drop_duplicates()
#
#     # Function that takes in movie title as input and outputs most similar movies
#     def get_recommendations(title, cosine_sim=cosine_sim):
#         # Get the index of the movie that matches the title
#         idx = indices[title]
#
#         # Get the pairwsie similarity scores of all movies with that movie
#         sim_scores = list(enumerate(cosine_sim[idx]))
#
#         # Sort the movies based on the similarity scores
#         sim_scores = sorted(sim_scores,  key=lambda x: x[1], reverse=True)
#
#         # Get the scores of the 10 most similar movies
#         sim_scores = sim_scores[1:11]
#
#         # Get the movie indices
#         movie_indices = [i[0] for i in sim_scores]
#
#         # Return the top 10 most similar movies
#         # return df_hearts['name'].iloc[movie_indices]
#         return df_hearts['id'].iloc[movie_indices]
#
#     list_ids = []
#     for i in list_recipe_filter:
#         ids = get_recommendations(i).values.tolist()
#         list_ids.append(ids)
#     final_ids = [659]
#     for i in list_ids_temp:
#         final_ids.append(i)
#     final_ids.append(660)
#     for i in list_ids:
#         for ii in i:
#             if ii not in final_ids:
#                 final_ids.append(ii)
#     # return get_recommendations(title).values.tolist()
#     remarks = ""
#     if len(final_ids) == 0:
#         for ii in list(TempHearts.objects.order_by("-total_hearts").values_list('id', flat=True)):
#             final_ids.append(ii)
#             remarks = "No related recipe found. Try our popular recipes instead!"
#
#     return [remarks, final_ids]