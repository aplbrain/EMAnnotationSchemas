import marshmallow as mm
from emannotationschemas.schemas.base import AnnotationSchema, BoundSpatialPoint


class BrainCircuitsBoundTagAnnotationUser(AnnotationSchema):
    pt = mm.fields.Nested(
        BoundSpatialPoint, required=True, description="Location associated with the tag"
    )
    tag = mm.fields.String(required=True, description="Arbitrary text tag")
    user_id = mm.fields.String(
        required=True,
        description=f"User who created the tag.",
    )

class RegionsOfInterest(AnnotationSchema):
    layer = fields.Boolean(description="Layer regions")
    brain_regions = fields.Boolean(description="Brain regions")
    cylinder = fields.Boolean(description="Cylinder regions")
    other = fields.String(description="Other regions of interest")
