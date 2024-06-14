import enum


class VerboseEnum(enum.Enum):
    def __new__(cls, value, verbose):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.verbose = verbose
        return obj


class Descriptor(VerboseEnum):
    """
    chem descriptor labels used in PARAM catalogue

    The first item in tuples bellow must not be changed, as it is used in the PARAM catalogue.
    The second item is a human-readable name.

    use:
    Descriptor.IUPAC.value
    Descriptor.IUPAC.verbose
    """

    OTHER_NAMES = ("otherNames", "Other Names")
    IUPAC = ("IUPAC", "IUPAC Name")
    MOLECULAR_FORMULA = ("MOLECULAR_FORMULA", "Molecular Formula")
    CAS = ("CAS", "CAS Number")
    SMILES_NOTATION = ("SMILES_NOTATION", "SMILES Notation")
    INCHI = ("INCHI", "InChI")
    ZOO_LABEL = ("zooLabel", "Zoo Label")
    CATEGORY = ("category", "Category")
    PEST_CLASS = ("pestClass", "Pesticide Class")
    DETAIL_LEVEL = ("detailLevel", "Detail Level")
    COM_ECSUBINVENTENTRYREF = (
        "COM_ECSUBINVENTENTRYREF",
        "COM EC Subinventory Entry Reference",
    )
    FLAVIS_NUMBER = ("FLAVIS_NUMBER", "Flavis Number")
