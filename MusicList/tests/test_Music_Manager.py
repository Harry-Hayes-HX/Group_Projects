import pytest
from ..lib.Music_Manager import *
import unittest
from unittest.mock import patch
from unittest.mock import Mock


class TestMenu():

    def test_Display_menu(self):
        #Create an instance of the Music class
        build = Music()

        #define expected output
        expected_output = "----------MENUS----------\n" \
            "1: Add music to list\n" \
            "2: List music on list\n" \
            "3: Quit\n"

        
        assert build.Display_menu() == expected_output


    @pytest.mark.parametrize("mocked_input, expected_choice", [("1\n", 1), ("2\n", 2), ("3\n", 3)])
    def test_valid_menu_input(self, mocked_input, expected_choice):
        #Create an instance of the Music class
        build = Music()

        #patch the input function to use the mocked input
        with patch('builtins.input', side_effect = mocked_input):
            #call the method that requires the user input
            user_choice = build.get_user_choice()

        assert user_choice == expected_choice

    @pytest.mark.parametrize("mocked_input", ["invalid\n", "4\n"])
    def test_invalid_menu_input(self, mocked_input):
        #Create an instance of the Music class
        build = Music()

        #patch the input function to use the mocked input
        with patch('builtins.input', side_effect = mocked_input):
            #call the method that requires the user input
            user_choice = build.get_user_choice()

        assert user_choice == None or "Invalid choice! please choose a valid menu option (1-3)"


class TestAdd():
    def test_add_valid_data(self):
        build = Music()
        data = {
            "I Prevail": ["Song 1", "Song 2", "Song 3"],
            "Foo Fighters": ["Song A", "Song B", "Song C"],
            "BMTH": ["Song X", "Song Y"]
        }

        expected_output = {
            "I Prevail": [["Song 1", "Song 2", "Song 3"]],
            "Foo Fighters": [["Song A", "Song B", "Song C"]],
            "BMTH": [["Song X", "Song Y"]]
        }

        for artists, songs in data.items():
            build.Add_music(artists, songs)

        result = build.List_music()
        assert isinstance(result, dict)

        for artists, songs in expected_output.items():
            assert artists in result
            assert result[artists] == songs


