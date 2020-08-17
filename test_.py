import pytest
from movie import Movie


def test_get_count():
    movie_graph = [[1], [0], [3], [2, 4], [3]]
    movie_list = {'good': 0, 'bad': 1, 'ok': 2, 'ok1': 3, 'ok2': 4}
    friend_list = ['a', 'b', 'c', 'd']
    friend_movie_list = {'a': ['ok', 'bad'], 'b': [
        'ok1', 'ok2'], 'c': ['ok2'], 'd': ['good']}
    recommendation = Movie(
        movie_list, friend_list, friend_movie_list, movie_graph)
    assert recommendation.getCount() == {
        'good': 1, 'bad': 1, 'ok': 1, 'ok1': 1, 'ok2': 2}


def test_get_discussability():
    movie_graph = [[1], [0], [3], [2, 4], [3]]
    movie_list = {'good': 0, 'bad': 1, 'ok': 2, 'ok1': 3, 'ok2': 4}
    friend_list = ['a', 'b', 'c', 'd']
    friend_movie_list = {'a': ['ok', 'bad'], 'b': [
        'ok1', 'ok2'], 'c': ['ok2'], 'd': ['good']}
    recommendation = Movie(
        movie_list, friend_list, friend_movie_list, movie_graph)
    count_dict = recommendation.getCount()
    assert recommendation.getDiscussability('good', count_dict) == 1
    assert recommendation.getDiscussability('bad', count_dict) == 1
    assert recommendation.getDiscussability('ok', count_dict) == 1
    assert recommendation.getDiscussability('ok1', count_dict) == 1
    assert recommendation.getDiscussability('ok2', count_dict) == 2


def test_same_component():
    movie_graph = [[1], [0], [3], [2, 4], [3]]
    movie_list = {'good': 0, 'bad': 1, 'ok': 2, 'ok1': 3, 'ok2': 4}
    friend_list = ['a', 'b', 'c', 'd']
    friend_movie_list = {'a': ['ok', 'bad'], 'b': [
        'ok1', 'ok2'], 'c': ['ok2'], 'd': ['good']}
    recommendation = Movie(movie_list, friend_list,
                           friend_movie_list, movie_graph)
    assert recommendation.sameComponent() == [1, 1, 2, 2, 2]


def test_get_similarity():
    movie_graph = [[1], [0], [3], [2, 4], [3]]
    movie_list = {'good': 0, 'bad': 1, 'ok': 2, 'ok1': 3, 'ok2': 4}
    friend_list = ['a', 'b', 'c', 'd']
    friend_movie_list = {'a': ['ok', 'bad'], 'b': [
        'ok1', 'ok2'], 'c': ['ok2'], 'd': ['good']}
    recommendation = Movie(movie_list, friend_list,
                           friend_movie_list, movie_graph)
    visited_color = recommendation.sameComponent()
    assert recommendation.getSimilarity('good', visited_color) == 0.25
    assert recommendation.getSimilarity('bad', visited_color) == 0.25
    assert recommendation.getSimilarity('ok', visited_color) == 0.75
    assert recommendation.getSimilarity('ok1', visited_color) == 0.75
    assert recommendation.getSimilarity('ok2', visited_color) == 0.5


def test_get_recommendation():
    movie_graph = [[1], [0], [3], [2, 4], [3]]
    movie_list = {'good': 0, 'bad': 1, 'ok': 2, 'ok1': 3, 'ok2': 4}
    friend_list = ['a', 'b', 'c', 'd']
    friend_movie_list = {'a': ['ok', 'bad'], 'b': [
        'ok1', 'ok2'], 'c': ['ok2'], 'd': ['good']}
    recommendation = Movie(movie_list, friend_list,
                           friend_movie_list, movie_graph)
    assert recommendation.getRecommendation() == 'good'
