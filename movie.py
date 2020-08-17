from typing import List
from typing import Dict


class Movie():
    def __init__(self,
                 movie_list: List[str],
                 friend_list: List[str],
                 friend_movie_list: Dict[str,
                                         List[str]],
                 movie_graph: List[List[int]]):
        """Constructor -- input value, movie_list that is a list of movies
        friend_list that is a list of user's friends,
        friend_movie_list is a dictionary that records a list of movie for each friend
        movie_graph is a 2 dimensional array that stores the similar movies for each movie in the movie list,
        in particular, if movie0 is similar to movie1, then movie_graph[0] has 1, we will use dfs to determine
        how these movies are connected, if they belong to the same component, they have the same color
        """
        self.movie_list = movie_list
        self.friend_list = friend_list
        self.friend_movie_list = friend_movie_list
        self.adj_list = movie_graph
        self.color = 1

    def getCount(self) -> Dict[str, List[str]]:
        """We will use a ditionary to keep track of how many friends
        have seen a movie in the movie_list"""
        count_of_movies = dict()
        for friend in self.friend_list:
            for movie in self.friend_movie_list[friend]:
                count_of_movies[movie] = count_of_movies.get(
                    movie, 0) + 1
        return count_of_movies

    def getDiscussability(
            self, movie: str, count_of_movies: Dict[str, int]) -> int:
        """We can get the discussability for a movie by taking the
        corresponding value for a key which is the name of the movie in 
        the dictionary"""
        if movie in count_of_movies:
            return count_of_movies[movie]
        else:
            return 0

    def dfs(self, v: int, color: int, visited: List[int]) -> None:
        """We use dfs to color each movie. If some of the movies are in 
        the same component, they share the same color in the visited array
        """
        visited[v] = color

        for u in self.adj_list[v]:
            if not visited[u]:
                self.dfs(u, color, visited)
        return

    def sameComponent(self) -> List[int]:
        """We traverse each movie in the movie list to determine their colors.
        """
        visited = [0 for i in range(len(self.adj_list))]
        for i in range(len(list(self.movie_list.values()))):
            if not visited[i]:
                self.dfs(i, self.color, visited)
                self.color += 1
        return visited

    def getSimilarity(self, movie: int, visited: List[int]) -> int:
        """We can calculate similarity for each movie in the movie_list.
        We compare the color of the movies in the friend_movie_list. If 
        they share the same color as the given movie, we increase the total
        by 1. To get similarity, we divide the total by the number of friends."""
        total = 0
        for friend in self.friend_list:
            for friend_movie in self.friend_movie_list[friend]:
                if visited[self.movie_list[friend_movie]
                           ] == visited[self.movie_list[movie]] and self.movie_list[friend_movie] != self.movie_list[movie]:
                    total += 1
        return total / len(self.friend_list)

    def getRecommendation(self) -> str:
        """We can get recommended movie with the highest discussability and
        uniqueness. For each movie in the movie_list, we obtain F/S, where 
        F is the discussability and S is the similarity."""
        maxValue = -float('inf')
        recommendedMovie = ''
        count_dict = self.getCount()
        visited_color = self.sameComponent()
        for key in self.movie_list.keys():
            F = self.getDiscussability(key, count_dict)
            S = self.getSimilarity(key, visited_color)
            if F / S > maxValue:
                maxValue = F / S
                recommendedMovie = key
        return recommendedMovie


if __name__ == '__main__':
    movie_graph = [[1], [0], [3], [2, 4], [3]]
    movie_list = {'good': 0, 'bad': 1, 'ok': 2, 'ok1': 3, 'ok2': 4}
    friend_list = ['a', 'b', 'c', 'd']
    friend_movie_list = {'a': ['ok', 'bad'], 'b': [
        'ok1', 'ok2'], 'c': ['ok2'], 'd': ['good']}
    recommendation = Movie(
        movie_list, friend_list, friend_movie_list, movie_graph)
    print(recommendation.getRecommendation())
