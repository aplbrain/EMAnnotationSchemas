from emannotationschemas.schemas.categorical_factories import BoundCategoricalFactory

schema_type_name = "extended_classical_cell_type"

allowed_cell_types = [
    "basket",
    "chandelier",
    "oligodendrocyte",
    "vip-i",
    "martinotti",
    "neurogliaform",
    "vip-chat",
    "vip-apical",
    "ivy",
    "clutch",
    "sst",
    "pyramidal",
    "uncertain",
]

category_name = "cell_type"
category_description = "cell type name"
class_name = "ExtendedClassicalCellType"

ExtendedClassicalCellType = BoundCategoricalFactory(
    allowed_cell_types,
    category_name,
    category_description,
    schema_type_name,
    class_name,
)

# Adding classes from https://github.com/aplbrain/BENCHMARK-Metadata/blob/1.1-and-1.2-annotation-metadata-for-review/annotation-metadata/CAVE-implemented-annotation-metadata-version-1.2.plantuml
# With explanations from here: https://github.com/aplbrain/BENCHMARK-Metadata/blob/1.1-and-1.2-annotation-metadata-for-review/annotation-metadata/required-field-names.md


