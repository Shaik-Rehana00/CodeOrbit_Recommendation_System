#CodeORbit Tech AI Internship
#Project 4: SImple Recommendation System
movies={
    "Inception":["Sci-Fi","Action","Thriller"],
    "Interstellar":["Sci-Fi","Adventure","Drama"],
    "The Dark Knight":["Action","Crime","Drama"],
    "Avengers":["Action","Sci-Fi","Adventure"],
    "Titanic":["Romance","Drama"],
    "the Martian":["Sci-Fi","Adventure","Drama"],
    "JOker":["Crime","Drama","Thriller"],
    "Avatar":["Sci-Fi","Action","Adventure"]
}

def recommend_movies(movie_name, top_n=3):
    if movie_name not in movies:
        print("Movie not found in data set.")
        return
    selected_genres = set(movies[movie_name])
    similarities=[]
    for title,genres in movies.items():
        if title==movie_name:
            continue
        other_genres=set(genres)
        common=len(selected_genres & other_genres)
        total=len(selected_genres|other_genres)
        score=common/total if total else 0

        similarities.append((title,score))
    similarities.sort(key=lambda item:item[1],reverse=True)
    print("\nRecommendation movies for:",movie_name)
    print("-"*40)
    count=0
    for title,score in similarities:
        if score>0 and count<top_n:
            print(f"{title}-Similarity:{score:.2f}")
            count+=1
print("=== CODEORBIT MOVIE RECOMMENDER ===")
print("\nAvailable movies:")
for title in movies:
    print(title)
choice=input("\nEnter a movie name:").strip()
recommend_movies(choice)