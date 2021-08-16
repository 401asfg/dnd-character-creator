from main.model.character.utility.enumerators.language import Language
from main.model.collection.collection_item import CollectionItem


_languages = {
    Language.COMMON: CollectionItem("Common Language"),
    Language.ELVISH: CollectionItem("Elvish Language"),
    Language.DWARVISH: CollectionItem("Dwarvish Language"),
    Language.GIANT: CollectionItem("Giant Language"),
    Language.GNOMISH: CollectionItem("Gnomish Language"),
    Language.GOBLIN: CollectionItem("Goblin Language"),
    Language.HALFLING: CollectionItem("Halfling Language"),
    Language.ORC: CollectionItem("Orc Language"),
    Language.ABYSSAL: CollectionItem("Abyssal Language"),
    Language.CELESTIAL: CollectionItem("Celestial Language"),
    Language.DRACONIC: CollectionItem("Draconic Language"),
    Language.DEEP_SPEECH: CollectionItem("Deep Speech"),
    Language.INFERNAL: CollectionItem("Infernal Language"),
    Language.PRIMORDIAL: CollectionItem("Primordial Language"),
    Language.SYLVAN: CollectionItem("Sylvan Language"),
    Language.UNDERCOMMON: CollectionItem("Undercommon Language")
}


def get_language(language: Language) -> CollectionItem:
    """
    Get the language trait

    :param language: The language whose trait to get
    :return: The language trait that corresponds to the given language
    """

    return _languages[language]


def get_darkvision() -> CollectionItem:
    """
    :return: The darkvision trait
    """

    return CollectionItem(
        "Darkvision",
        "You can see in dim light within 60 ft. of you as if it were bright light, and in darkness as if it were dim "
        "light."
    )


def get_fey_ancestry() -> CollectionItem:
    """
    :return: The fey ancestry trait
    """

    return CollectionItem(
        "Fey Ancestry",
        "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."
    )
