import marshmallow as mm
from emannotationschemas.schemas.base import (
    AnnotationSchema,
    BoundSpatialPoint,
    ReferenceAnnotation,
)


class FunctionalCoregistration(AnnotationSchema):
    pt = mm.fields.Nested(
        BoundSpatialPoint,
        required=True,
        description="location of cell body of functional cell",
    )
    func_id = mm.fields.Int(required=True, description="functional cell ID")


class FunctionalUnitCoregistration(AnnotationSchema):
    pt = mm.fields.Nested(
        BoundSpatialPoint,
        required=True,
        description="location of cell body of functional cell",
    )
    session = mm.fields.Int(required=True, description="session ID of imaging")
    scan_idx = mm.fields.Int(
        required=True, description="index of the scan within the session"
    )
    unit_id = mm.fields.Int(
        required=True, description="unique functional cell ID within the scan"
    )


class FunctionalUnitCoregistrationExtended(ReferenceAnnotation):
    session = mm.fields.Int(required=True, description="session ID of imaging")
    scan_idx = mm.fields.Int(
        required=True, description="index of the scan within the session"
    )
    unit_id = mm.fields.Int(
        required=True, description="unique functional cell ID within the scan"
    )
    field = mm.fields.Int(
        required=False, description="index of imaging field of cell within the scan"
    )
    residual = mm.fields.Float(
        required=False,
        description="distance between nucleus centroid and functional centroid after transformation",
    )
    score = mm.fields.Float(
        required=False, description="confidence score associated with match"
    )

# Adding classes from https://github.com/aplbrain/BENCHMARK-Metadata/blob/1.1-and-1.2-annotation-metadata-for-review/annotation-metadata/CAVE-implemented-annotation-metadata-version-1.2.plantuml
# With explanations from here: https://github.com/aplbrain/BENCHMARK-Metadata/blob/1.1-and-1.2-annotation-metadata-for-review/annotation-metadata/required-field-names.md

class CoRegistration(ReferenceAnnotation):
    valid = fields.Boolean(description="Indicates if the co-registration is valid")
    pt = fields.Nested('PointSchema', description="Point schema for location data")
    valid_id = fields.Float(description="Validation ID")
    status_dendrite = fields.String(description="Status of the dendrite")
    object_id = fields.String(description="Object ID for co-registration")
    other = fields.String(description="Other co-registration-related information")

# Moving this to the bottom/after BENCHMARK additions:
class FunctionalUnitCoregistrationQC(ReferenceAnnotation):
    pass
