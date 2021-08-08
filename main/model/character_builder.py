from typing import Callable, Type, Tuple, Union

from main.model.character.class_ import Class
from main.model.character.race import Race
from main.model.int_types.natural import Natural

_races = (

)

_classes = (

)


class CharacterBuilder:
    """
    Manages the character creation process
    """

    def __init__(self):
        """
        Initializes the class
        """

        # TODO: refactor prompt generators into an inner method

        race_setter_prompt = ""

        for i in range(0, len(_races)):
            race_setter_prompt += str(i + 1) + " - " + _races[i].get_name() + "\n"

        race_setter_prompt += "Enter the character's race index:"

        class_setter_prompt = ""

        for i in range(0, len(_classes)):
            class_setter_prompt += str(i + 1) + " - " + _classes[i].get_name() + "\n"

        class_setter_prompt += "Enter the character's class index:"

        self._name: str
        self._age: Natural
        self._race: Race
        self._class: Class

        # TODO: make sure documentation is correct

        def parameter_setter(
                exception_types: Union[Tuple[Type[Exception], ...], Tuple],
                error_feedback: str,
                next_prompt: str,
                next_parameter_setter: Callable[[], None]
        ):
            """
            Convert a function to be a parameter_setter

            :param exception_types: The exceptions that, if raised by the function, cause the next feedback to be set to
            the error_feedback and prevents both the next prompt and next operation from being set to the given values
            :param error_feedback: The message to set next feedback to should one of the exception_types be caught
            :param next_prompt: The message to set the next prompt to should no exception be caught
            :param next_parameter_setter: The function to call should no exception be caught
            :return: A function that will return a function that will call the converted function
            """

            def get_caller(fn: Callable[[str], None]):
                """
                Gets a function that will call the given fn

                :param fn: The function to be called by the returned function
                :return: The quit_on_exception inner function
                """

                def quit_on_exception(fn_value: str):
                    """
                    Tries to call the given fn with the given fn_value as its only parameter; if it succeeds, sets the
                    next feedback to a confirmation response, the next prompt to the given next_prompt, and the next
                    operation to given next_operation; if one of the given exception_types are caught, sets the next
                    feedback to error_feedback

                    :param fn_value: The value to pass to the given fn
                    """

                    try:
                        fn(fn_value)

                        self._next_feedback = "The response: " + fn_value + " was accepted."
                        self._next_prompt = next_prompt
                        self._next_parameter_setter = next_parameter_setter
                    except exception_types:
                        self._next_feedback = error_feedback

                return quit_on_exception

            return get_caller

        @parameter_setter(
            (ValueError, IndexError),
            "The entered class index was not within acceptable bounds.",
            None,
            None
        )
        def set_class(value: str):
            """
            Sets the character's class to a class in the class list that is at the given value - 1; raises ValueError if
            value is not an integer; raises IndexError if value is less than 0 or greater than or equal to the number of
            races

            :param value: The index + 1 of the class in the class list that the character's class will be set to
            """
            self._class = _classes[int(value) - 1]

        @parameter_setter(
            (ValueError, IndexError),
            "The entered race index was not within acceptable bounds.",
            class_setter_prompt,
            set_class
        )
        def set_race(value: str):
            """
            Sets the character's race to a race in the race list that is at the given value - 1; raises ValueError if
            value is not an integer; raises IndexError if value is less than 0 or greater than or equal to the number of
            races

            :param value: The index + 1 of the race in the race list that the character's race will be set to
            """

            self._race = _races[int(value) - 1]

        @parameter_setter(
            (ValueError,),
            "The entered age was not within acceptable bounds.",
            race_setter_prompt,
            set_race
        )
        def set_age(value: str):
            """
            Set the age to the given value; raises ValueError if value is not an integer or is less than 0

            :param value: The value to set the age to
            """

            self._age = Natural(int(value))

        @parameter_setter((), "", "Enter the character's age (can be a positive number):", set_age)
        def set_name(value: str):
            """
            Set the name to the given value

            :param value: The value to set the name to
            """

            self._name = value

        self._next_prompt: str = "Enter the character's name:"
        self._next_parameter_setter: Callable[[str], None] = set_name
        self._next_feedback: str = ""

    @property
    def next_prompt(self) -> str:
        return self._next_prompt

    @property
    def next_parameter_setter(self) -> Callable[[str], None]:
        return self._next_parameter_setter

    @property
    def next_feedback(self) -> str:
        return self._next_feedback

    @property
    def races(self) -> Tuple[Type[Race], ...]:
        return _races

    @property
    def classes(self) -> Tuple[Type[Class], ...]:
        return _classes
